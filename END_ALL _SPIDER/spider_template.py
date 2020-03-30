from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import sqlite3
import os
import urllib.request
import time

class MySpider:
    headers = {
        "User - Agent": "Mozilla / 5.0(Linux;Android 6.0;Nexus 5  Build / MRA58N) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.3904.108 Mobile Safari / 537.36"
    }
    imagePath = "dowmload"

    def startUp(self):
        # 初始化一个浏览器
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()   #最大化窗口

        self.threads = []  # 装入线程
        self.No = 0  # 数据编号

        # 初始化一个数据库和一个表
        try:
            self.con = sqlite3.connect("phones.db")
            self.cursor = self.con.cursor()
            try:
                self.cursor.execute("drop table phone")
            except:
                pass

            try:
                sql = '''
                create table phone
                
                
                '''
                self.cursor.execute(sql)
            except:
                pass
        except Exception as err:
            print(err)

        #检查图片文件夹是否存在，不存在创建，存在删除里面的文件
        try:
            if not os.path.exists(MySpider.imagePath):
                os.mkdir(MySpider.imagePath)
            images = os.listdir(MySpider.imagePath)
            for img in images:
                s = os.path.join(MySpider.imagePath, img)
                os.remove(s)
        except Exception as err:
            print(err)


    def closeUp(self):
        try:
            self.con.commit()   #提交事务
            self.con.close()     #关闭数据库
            self.driver.close()  #关闭浏览器
        except Exception  as err:
            print(err)

    def insertDB(self,no, mark, price,mfile):
        try:
            sql = "insert into phones(no,marik, price, mfile) values (?,?,?,?)"
            self.cursor.execute(sql, (no, mark, price,mfile))
        except Exception as err:
            print(err)


    def showDB(self):
        try:
            print("%-8s %-16s %-16s" % ("no", "mark" ,"price","mfile"))
            self.cursor.execute("select * from phones")
            rows = self.cursor.fetchall()   #获取查找的数据
            for row in rows:
                print("%-8s %-16s %-16s %-16s" % (row[0],row[1],row[2],row[3]))
        except Exception as err:
            print(err)


    def download(self,src,mfile):
        try:
            req = urllib.request.Request(src, headers=self.headers)
            data = urllib.request.urlopen(req, timeout=400)  #访问网站最多400毫秒
            data = data.read()
            fobj = open(MySpider.imagePath + "\\" + mfile, "wb")
            fobj.write(data)
            fobj.close()
        except Exception as err:
            print(err)

    def processSpider(self):
        try:
            print(self.driver.current_url)

            #找到所有class=‘phone'的div
            divs = self.driver.find_elements_by_xpath("//div[@class='phone']")
            for div in divs:
                src = div.find_element_by_xpath(".//img").get_attribute("src")
                src = urllib.request.urljoin(self.driver.current_url, src)
                mark = div.find_element_by_xpath(".//div[position()=3").text
                price = div.find_element_by_xpath(".//div[position()=4").text

                self.No +=1
                #数据编号
                no =  str(self.No)
                if len(no) < 6:
                    no = "0" + no

                #图片名  编号+图片后缀
                p = src.rindex(".")
                mfile = no + src[p:]


                self.insertDB(no,mark,price,mfile)

                #开启线程下载图片,调用download方法，传入图片地址和新的名字
                T = threading.Thread(target=self.download,args=[src, mfile])
                T.start()
                self.threads.append(T)

            #显示翻页
            try:
                next_pase = self.driver.find_elements_by_xpath("//div[@class='paging']//input[@type='button']")[-2]
                #按钮是否可用
                if next_pase.is_enabled():
                    next_pase.click()
                    time.sleep(0.1)
                    self.processSpider()
            except Exception as err:
                print(err)
        except Exception as err:
            print(err)


    def executeSpider(self, url):
        print("Spider starting .....")
        self.startUp()
        self.driver.get(url)
        self.processSpider()
        for t in self.threads:
            t.join()
        self.showDB()
        self.closeUp()
        print("Spider end ......")

spider = MySpider()
spider.executeSpider("http.//3535254")
