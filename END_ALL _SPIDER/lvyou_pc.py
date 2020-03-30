from bs4 import BeautifulSoup
import urllib.request

doc = '''
<div class="sightlist">
<div class="sightshow">
    <div class="sightimg"><a href="http://scenic.cthy.com/scenic-14115/"><img src="http://scenic.cthy.com/UploadPic/PhotoAlbum_Images/JingQu/635335033534313698.jpg" width="115" height="72" alt="珠海长隆国际海洋度假区"></a></div>
         <div class="sightdetail">
        <h4><a href="http://scenic.cthy.com/scenic-14115/" target="_blank">珠海长隆国际海洋度假区</a></h4>
        <ul class="sightbase">
            <li>景区类型：<a href="/scenicSearch/0-101-0-0-0-1.html" target="_blank" class="ls">海滨海岛</a> <a href="/scenicSearch/0-105-0-0-0-1.html" target="_blank" class="ls">生物景观</a> </li>
            <li>景区资质：<a href="/scenicSearch/0-0-0-301-0-1.html" target="_blank" class="ls">国家级风景名胜区</a></li>
            <li><span>景区级别：<a href="/scenicSearch/0-0-201-0-0-1.html" target="_blank" class="ls">5A</a></span>适合季节：<a href="/scenicSearch/0-0-0-0-405-1.html" target="_blank" class="ls">四季皆宜</a> </li>
        </ul>
        <ul class="sighthotel">
            <li>
                <span>¥0</span>
                <a href="http://hotel.cthy.com/hotelinfo-68151/" target="_blank" title="珠海海泉湾海洋温泉中心">珠海海泉湾海洋温泉中心</a>
            </li>
            <li>
                <span>¥230</span>

                <a href="http://hotel.cthy.com/hotelinfo-8498/" target="_blank" title="珠海海泉湾客栈">珠海海泉湾客栈</a>
            </li>
                <li><span>¥700</span>
                <a href="http://hotel.cthy.com/hotelinfo-4564/" target="_blank" title="珠海海泉湾维景大酒店">珠海海泉湾维景大酒店</a>
            </li>
        </ul>
    </div>
    <div class="sightshow">
    <div class="sightimg"><a href="http://scenic.cthy.com/scenic-14115/"><img src="http://scenic.cthy.com/UploadPic/PhotoAlbum_Images/JingQu/635335033534313698.jpg" width="115" height="72" alt="珠海长隆国际海洋度假区"></a></div>
         <div class="sightdetail">
        <h4><a href="http://scenic.cthy.com/scenic-14115/" target="_blank">珠海长隆国际海洋度假区</a></h4>
        <ul class="sightbase">
            <li>景区类型：<a href="/scenicSearch/0-101-0-0-0-1.html" target="_blank" class="ls">海滨海岛</a> <a href="/scenicSearch/0-105-0-0-0-1.html" target="_blank" class="ls">生物景观</a> </li>
            <li>景区资质：<a href="/scenicSearch/0-0-0-301-0-1.html" target="_blank" class="ls">国家级风景名胜区</a></li>
            <li><span>景区级别：<a href="/scenicSearch/0-0-201-0-0-1.html" target="_blank" class="ls">5A</a></span>适合季节：<a href="/scenicSearch/0-0-0-0-405-1.html" target="_blank" class="ls">四季皆宜</a> </li>
        </ul>
        <ul class="sighthotel">
            <li>
                <span>¥0</span>
                <a href="http://hotel.cthy.com/hotelinfo-68151/" target="_blank" title="珠海海泉湾海洋温泉中心">珠海海泉湾海洋温泉中心</a>
            </li>
            <li>
                <span>¥230</span>

                <a href="http://hotel.cthy.com/hotelinfo-8498/" target="_blank" title="珠海海泉湾客栈">珠海海泉湾客栈</a>
            </li>
                <li><span>¥700</span>
                <a href="http://hotel.cthy.com/hotelinfo-4564/" target="_blank" title="珠海海泉湾维景大酒店">珠海海泉湾维景大酒店</a>
            </li>
        </ul>
    </div>
    <div class="sightshow">
    <div class="sightimg"><a href="http://scenic.cthy.com/scenic-14115/"><img src="http://scenic.cthy.com/UploadPic/PhotoAlbum_Images/JingQu/635335033534313698.jpg" width="115" height="72" alt="珠海长隆国际海洋度假区"></a></div>
         <div class="sightdetail">
        <h4><a href="http://scenic.cthy.com/scenic-14115/" target="_blank">珠海长隆国际海洋度假区</a></h4>
        <ul class="sightbase">
            <li>景区类型：<a href="/scenicSearch/0-101-0-0-0-1.html" target="_blank" class="ls">海滨海岛</a> <a href="/scenicSearch/0-105-0-0-0-1.html" target="_blank" class="ls">生物景观</a> </li>
            <li>景区资质：<a href="/scenicSearch/0-0-0-301-0-1.html" target="_blank" class="ls">国家级风景名胜区</a></li>
            <li><span>景区级别：<a href="/scenicSearch/0-0-201-0-0-1.html" target="_blank" class="ls">5A</a></span>适合季节：<a href="/scenicSearch/0-0-0-0-405-1.html" target="_blank" class="ls">四季皆宜</a> </li>
        </ul>
        <ul class="sighthotel">
            <li>
                <span>¥0</span>
                <a href="http://hotel.cthy.com/hotelinfo-68151/" target="_blank" title="珠海海泉湾海洋温泉中心">珠海海泉湾海洋温泉中心</a>
            </li>
            <li>
                <span>¥230</span>

                <a href="http://hotel.cthy.com/hotelinfo-8498/" target="_blank" title="珠海海泉湾客栈">珠海海泉湾客栈</a>
            </li>
                <li><span>¥700</span>
                <a href="http://hotel.cthy.com/hotelinfo-4564/" target="_blank" title="珠海海泉湾维景大酒店">珠海海泉湾维景大酒店</a>
            </li>
        </ul>
    </div>
</div>


</div>
'''
import sqlite3
import json
import time


class Myspider:
    start_url = "http://scenic.cthy.com/scenicSearch/0-0-201-0-0-1.html"

    def __init__(self):
        req = urllib.request.urlopen(Myspider.start_url)
        data = req.read().decode()
        self.soup = BeautifulSoup(data, "html.parser")
        self.no = 0
        self.aa = []
    def openDB(self):
        self.con = sqlite3.connect("fengjing.db")
        self.cursor = self.con.cursor()

    def initDB(self):
        try:
            self.cursor.execute("drop table fengjing")
        except:
            pass
        try:
            self.cursor.execute(
                "create table fengjing(no varchar(8) primary key , name varchar(300), type varchar(100), zhiz varchar(60), season var(10),class varchar(4),hotel varchar(100))")
        except:
            self.cursor.execute("drop table fengjing")

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insert(self, n, name, type, zhiz, season, Class, hotel):
        try:
            self.cursor.execute("insert into fengjing(no,name,type,zhiz,season,class,hotel) values (?,?,?,?,?,?,?)",
                                (n, name, json.dumps(type), zhiz, season, Class, json.dumps(hotel)))
        except Exception as err:
            print(err)

    def showDB(self):
        self.cursor.execute("select * from fengjing")
        rows = self.cursor.fetchall()
        for row in rows:
            print("No", row[0])
            print("名称:", row[1], "时间:", row[4], "级别:", row[5])
            types = json.loads(row[2])
            print("类型:", end="")
            for t in types:
                print(t, end="")
            print()
            hotels = json.loads(row[6])
            print("酒店:")
            for h in hotels:
                print(h["hotel"], h["price"])
            print()

    def show(self):
        self.openDB()
        self.showDB()
        self.closeDB()

    def spider(self):
        divs = self.soup.find("div", attrs={'class': 'sightlist'}).find_all("div", attrs={'class': 'sightshow'})
        # divs = soup.select("div[class='sightlist'] div[class='sightshow']")
        for div in divs:
            self.no += 1
            dd = div.find("div", attrs={'class': 'sightdetail'})
            name = dd.find("h4").find("a").text
            lis = dd.find("ul", attrs={'class': 'sightbase'}).find_all("li")
            types = lis[0].find_all("a")
            type = []
            if len(types):
                for t in types:
                    type.append(t.text)
            zhiz = lis[1].find("a").text
            jb = lis[2].find_all("a")
            jibie = jb[0].text
            jijie = jb[1].text

            hlis = dd.find("ul", attrs={'class': 'sighthotel'}).find_all("li")
            hs = []
            for i in range(len(hlis)):
                h = {}
                h['price'] = hlis[i].find("span").text
                h['hotel'] = hlis[i].find("a").text
                hs.append(h)
            self.insert(self.no, name, type, zhiz, jijie, jibie, hs)
            print(self.no, name, type, zhiz, jijie, jibie, hs)

        # a = self.soup.find("ul", attrs={'id': 'PagerList'}).find_all("li").find("a",attrs={'alt':'下页'})
        a = self.soup.find(alt="下页")["href"]

        if a not in self.aa:
            self.aa.append(a)
            url = urllib.request.urljoin(Myspider.start_url, a)
            data = urllib.request.urlopen(url).read().decode()
            self.soup = BeautifulSoup(data, "html.parser")
            self.spider()

    def process(self):
        print("spider......")
        self.openDB()
        self.initDB()
        self.spider()
        self.showDB()
        self.closeDB()
        print("spider end")


myspider = Myspider()

while 1:
    print("1.开始爬虫")
    print("2.显示数据")
    print("3.退出")
    c = input("请输入(1,2,3)操作数字：")
    if c == "1":
        myspider.process()
    elif c == "2":
        myspider.show()
        time.sleep(20)
    elif c == "3":
        break