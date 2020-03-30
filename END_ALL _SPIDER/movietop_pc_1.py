from bs4 import BeautifulSoup
import bs4.element
import urllib.request
import sqlite3
import threading
import json
import random


class MySpider:
    header_list = [
        "Mozilla / 5.0(Windows NT 6.1; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.3904.108 Safari / 537.36"
        " Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 535.1(KHTML, like Gecko) Chrome / 14.0835.163 Safari / 535.1"
        "Mozilla / 5.0(Macintosh; Intel Mac OSX10_7_0) AppleWebKit / 535.11(KHTML, like Gecko) Chrome / 17.0.963.56 Safari / 535.11"
        "Opera / 9.80(Windows NT 6.1; U ; en) Presto / 2.8.131 Version / 11.11"
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ]
    start_url = 'https://movie.douban.com/top250'
    imagePath = "images"

    def __init__(self):
        self.thraeds = []
        self.No = 0

    def openDB(self):
        self.con = sqlite3.connect("movieTop.db")
        self.cursor = self.con.cursor()

    def closeDB(self):
        self.con.commit()
        self.cursor.close()

    def initDB(self):
        try:
            self.cursor.execute("drop table movieTop")
        except:
            pass
        try:
            sql = '''
            create table movieTop(
            mTitle varchar(256) primary key, mDirector varchar(30), 
            mActor varchar(256),mTime varchar(4),mCountry varchar(20), 
            mType varchar(30), mRatingnum float, mQueto varchar(256)
            )        
            '''
            self.cursor.execute(sql)
        except Exception as err:
            print(err)

    def showDB(self):
        try:
            self.cursor.execute("select *from movieTop")
            rows = self.cursor.fetchall()
            no = 0
            for row in rows:
                no += 1
                print("No.", no)
                print("电影:", json.loads(row[0]))
                print("导演:", row[1], "  主演:", row[2])
                print(row[3] + "/" + row[4] + "/" + row[5])
                print("评分:", row[6], end="")
                print(row[7])
        except Exception as err:
            print(err)

    def show(self):
        self.openDB()
        self.showDB()
        self.closeDB()

    def insertBD(self, title, director, actor, time, country, type, ratingnum, quote):
        try:
            sql = '''
                insert into movieTop(
            mTitle , mDirector, 
            mActor, mTime, mCountry, 
            mType, mRatingnum, mQueto) values (?,?,?,?,?,?,?,?)
            '''
            self.cursor.execute(sql, (title, director, actor, time, country, type, ratingnum, quote))
        except Exception as err:
            print(err)

    def spider(self, url):
        req = urllib.request.Request(url, headers={"User-Agent":random.choice(MySpider.header_list)})
        req = urllib.request.urlopen(req)
        data = req.read().decode()
        soup = BeautifulSoup(data, "html.parser")
        lis = soup.select("ol[class='grid_view'] li")
        for li in lis:
            self.No += 1
            titles = li.select("div[class='hd'] a span")
            title = []
            for t in range(len(titles)):
                tt = titles[t].text.strip().strip("\n")
                title.append(tt)
            p = li.select("div[class='bd'] p")[0]
            res = self.spiderMarkerMovieInfo(p)
            director = res[0] if res[0] else ""
            actor = res[1] if res[1] else ""
            mtime = res[2]
            country = res[3]
            mtype = res[4]
            img = li.select("img")[0].get("src")
            T = threading.Thread(target=self.download, args=[img,str(self.No)])
            T.start()
            self.thraeds.append(T)

            rating_num = li.select("span[class='rating_num']")[0].text
            try:
                quote = li.select("span[class='inq']")[0].text
            except:
                quote=""

            self.insertBD(json.dumps(title), director, actor, mtime, country, mtype, rating_num, quote)

        try:
            next_page = soup.select("div[class='paginator'] span[class='next'] a")[0].get("href")
            if next_page:
                url = urllib.request.urljoin(MySpider.start_url, next_page)
                self.spider(url)
        except:
            pass

    def download(self, url,no):
        q = url.rindex(".")
        ext = url[q:]
                                                                #random.choice(list) 随机取list中一个值
        req = urllib.request.Request(url,headers={"User-Agent":random.choice(MySpider.header_list)})
                                        #timeout 响应时间超过5秒就不访问
        data = urllib.request.urlopen(req,timeout=5).read()
        fobj = open(MySpider.imagePath+"/" + no + ext,"wb")
        fobj.write(data)
        fobj.close()
        print("download", no + ext)

    def spiderMarkerMovieInfo(self, p):
        res = []
        flag = True
        for c in p.children:
            # 判断C是不是bs4.element.NavigableString类型,是不是字符串
            if isinstance(c, bs4.element.NavigableString):
                t = c.string.strip("\n").strip()
                if t != "":
                    if flag:
                        pos = t.find("主演")
                        director = t[:pos].replace("导演:", "")
                        actor = t[pos + 3:]
                        res.append(director)
                        res.append(actor)
                    else:
                        st = t.split("/")
                        for e in st:
                            res.append(e)
                        break
            # 判断c是不是bs4.element.Tag类型，是不是标签  并且c标签为<br>
            elif isinstance(c, bs4.element.Tag) and c.name == "br":
                flag = False
        return res

    def process(self, url):
        print("spider......")
        self.openDB()
        self.initDB()
        self.spider(url)
        for t in self.thraeds:
            t.join()
        print("spider end...")
        self.showDB()
        self.closeDB()



myspider = MySpider()
start_url = 'https://movie.douban.com/top250'
myspider.process(start_url)
