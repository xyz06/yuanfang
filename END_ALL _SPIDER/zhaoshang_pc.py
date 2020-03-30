import urllib.request
from bs4 import BeautifulSoup
import sqlite3


class MySpider:
    def openDB(self):
        self.con = sqlite3.connect("zhaoshang.db")
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("drop table rates")
        except:
            pass
        self.cursor.execute(
            "create table rates(Currency varchar(100) primary key, TSP float,CSP float,TBP float, CBP float, Time varchar(100))")

    def closeDB(self):
        self.con.commit();
        self.cursor.close()

    def insert(self,n,t,c,tb,cb,time):
        try:
            self.cursor.execute("insert into rates(Currency,TSP,CSP,TBP,CBP,Time) values (?,?,?,?,?,?)",(n,t,c,tb,cb,time))
        except Exception as err:
            print(err)

    def showDB(self):
        try:
            self.cursor.execute("select  * from rates")
            data = self.cursor.fetchall()
            print("%-16s %-8s %-8s %-8s %-8s %-8s " % ("Currency","TSP","CSP","TBP","CBP","Time"))
            for d in data:
                print("%-16s %-8s %-8s %-8s %-8s %-8s " % (d[0],d[1],d[2],d[3],d[4],d[5]))
        except Exception as err:
            print(err)


    def process(self,url):
        req = urllib.request.urlopen(url)
        data = req.read().decode()
        soup = BeautifulSoup(data, "html.parser")
        trs = soup.select("div[id='realRateInfo'] table tr")
        for i in range(0, len(trs)):
            tds = trs[i].select("td")
            n = tds[0].text.strip()
            t = tds[3].text.strip()
            c = tds[4].text.strip()
            tb = tds[5].text.strip()
            cb =tds[6].text.strip()
            time = tds[7].text.strip()
            self.insert(n,t,c,tb,cb,time)

url = "http://fx.cmbchina.com/hq/"
myspider = MySpider()
myspider.openDB()
myspider.process(url)
myspider.showDB()
myspider.closeDB()


