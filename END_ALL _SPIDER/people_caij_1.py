from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import time

class MySpider:
    No = 0
    start_url = "http://finance.people.com.cn/index1.html#fy01"

    def getAllText(self,url):
        url = urllib.request.urljoin(MySpider.start_url,url)
        req = urllib.request.urlopen(url)
        data = req.read()
        dammit = UnicodeDammit(data, ["UTF-8", "GBK"])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, "html.parser")
        pText = soup.select("div[class='box_con'] p")
        print("详情：")
        for p in pText:
            print(p.text)

    def spider(self,url):
        req = urllib.request.urlopen(url)
        data = req.read()
        dammit = UnicodeDammit(data,["UTF-8","GBK"])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, "html.parser")
        hds = soup.select("div[class='headingNews qiehuan1_c'] div[class='hdNews clearfix']")
        for hd in hds:
            MySpider.No +=1
            title = hd.select("h5")[0].text
            cText = hd.select("em")[0].text
            cAtext = hd.select("h5 a")[0]["href"]
            print(MySpider.No)
            print("标题:",title)
            print("正文:",cText)
            self.getAllText(cAtext)
            print()

        hdl = soup.select("div[class='headingNews qiehuan1_c'] div[class='page_n clearfix']")[-1]
        try:
            next_page = hdl.select("a")[-1]
            if next_page.text == "下一页":
                url = urllib.request.urljoin(MySpider.start_url, next_page["href"])
                self.spider(url)
                time.sleep(4)
        except:
            print("Spider End....")
            pass


caijin = MySpider()
caijin.spider(caijin.start_url)
