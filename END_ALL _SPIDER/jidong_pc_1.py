from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import threading
import os
import sqlite3
import socket
import random

class MySpider:
    #header = {
    #    "User - Agent": "Mozilla / 5.0(Linux;Android 6.0;Nexus 5  Build / MRA58N) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.3904.108 Mobile Safari / 537.36"
    #}
    #改良
    ua_list = [
        "Mozilla / 5.0(Windows NT 6.1; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.3904.108 Safari / 537.36"
        " Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 535.1(KHTML, like Gecko) Chrome / 14.0835.163 Safari / 535.1"
        "Mozilla / 5.0(Macintosh; Intel Mac OSX10_7_0) AppleWebKit / 535.11(KHTML, like Gecko) Chrome / 17.0.963.56 Safari / 535.11"
        "Opera / 9.80(Windows NT 6.1; U ; en) Presto / 2.8.131 Version / 11.11"
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ]

    imagesPath = "jdImages"

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.no = 0
        self.theards = []

        if os.path.exists(MySpider.imagesPath):
            s = os.listdir(MySpider.imagesPath)
            for i in s:
                p = os.path.join(MySpider.imagesPath, i)
                os.remove(p)
        else:
            os.mkdir(MySpider.imagesPath)

        try:
            self.con = sqlite3.connect("phones.db")
            self.cursor = self.con.cursor()
            self.cursor.execute("create table phones(no varchar(6) primary key, mark varchar(256),price varchar(16),image varchar(256))")
        except:
            self.cursor.execute("drop table phones")


    def readlySpider(self, url):
        self.driver.get(url)
        ipt = self.driver.find_element_by_id("key")
        ipt.send_keys("手机")
        ipt.send_keys(Keys.ENTER)
        time.sleep(4)

    def download(self, src, mfile):
        try:
            src = urllib.request.urljoin(self.driver.current_url, src)
            req = urllib.request.Request(src, headers={"User-Agent":random.choice(MySpider.ua_list)})
            data = urllib.request.urlopen(req,timeout=5)
            dat = data.read()
            data.close()
            ofbj = open(MySpider.imagesPath + "//" + mfile, "wb")
            ofbj.write(dat)
            ofbj.close()
            time.sleep(0.5)

        except Exception as err:
            print(err)



    def jdSpider(self):
       # socket.setdefaulttimeout(20)
        print(self.driver.current_url)
        # ipt = driver.find_element_by_xpath("//div[@class='jd-header-search-input']//input[@id='msKeyWord']")
        lis = self.driver.find_elements_by_xpath("//div[@id='J_goodsList']/ul/li")
        for li in lis:
            self.no += 1
            price = li.find_element_by_xpath(".//div[@class='p-price']/strong/i").text
            img = li.find_element_by_xpath("//div[@class='p-img']//a//img").get_attribute("src")
            p = img.rindex(".")
            p = img[p:]
            mfile = str(self.no) + p

            note = li.find_element_by_xpath("//div[@class='p-name p-name-type-2']//a//em").text
            try:
                mark = note.split()[0]
                note.replace("【新品抢购】", "")
            except:
               mark = " "
               note = " "
            print(self.no,mark, price, mfile)

            T = threading.Thread(target=self.download,args=[img,mfile])
            T.start()
            self.theards.append(T)

        try:
            next_page = self.driver.find_element_by_xpath(
                "//div[@id='J_bottomPage']/span[@class='p-num']/a[@class='pn-next']")
            next_page.click()
            time.sleep(5)
            self.jdSpider()
        except:
            print("end")


# no = 0
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# ipt = driver.find_element_by_xpath("//div[@class='jd-header-search-input']//input[@id='msKeyWord']")
# ipt = driver.find_element_by_id("key")
# ipt.send_keys("手机")
# ipt.send_keys(Keys.ENTER)
# jdSpider(driver)


jdspider = MySpider()
jdspider.readlySpider("https://www.jd.com")
jdspider.jdSpider()
for t in jdspider.theards:
    t.join()

