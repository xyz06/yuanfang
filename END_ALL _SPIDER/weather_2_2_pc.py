import sqlite3
import urllib.request
from bs4 import UnicodeDammit
from bs4 import BeautifulSoup

class WeatherDB:
    def openDB(self):
        self.con = sqlite3.connect("weathers.db")
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("create table weatherss(wcity varchar(16), wdate varchar(16), wweather varchar(18), \
                                wtem varchar(32), constraint p_k_code primary key (wcity, wdate))" )
        except:
            self.cursor.execute("delete from weatherss")


    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insert(self,wcity, wdate, wweather, wtem):
        try:
            self.cursor.execute("insert into weatherss(wcity, wdate, wweather, wtem) values (?,?,?,?)",( wcity, wdate, wweather, wtem) )
        except Exception as err:
            print(err)

    def show(self):
        try:
            self.cursor.execute("select * from weatherss")
            rows = self.cursor.fetchall()
            print("%-16s %-16s %-20s %-16s " % ("city", "date", "weather", "tem"))
            for row in rows:
                print("%-16s %-16s %-20s %-16s " % (row[0], row[1], row[2], row[3]))
        except Exception as err:
            print(err)


class weatherForecast:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, \
                                 like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
        }
        self.cityCode = {"北京":"101010100", "上海":"101020100", "广州":"101280101", "深圳":"101280601"}

    def forecasteWeather(self,city):
        if city not in self.cityCode.keys():
            print(city + "不在查看范围")
            return
        try:
            url = "http://www.weather.com.cn/weather/" + self.cityCode[city] + ".shtml"
            req  = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req)
            data = data.read()
            dammit = UnicodeDammit(data, ['utf-8','gbk'])
            data = dammit.unicode_markup
            soup = BeautifulSoup(data,"html.parser")
            lis = soup.select("ul[class='t clearfix'] li")
            for li in lis:
                try:
                    date = li.select("h1")[0].text
                    weather = li.select("p[class='wea']")[0].text
                    tem = li.select("p[class='tem'] span")[0].text + "/" + li.select("p[class='tem'] i")[0].text
                    print(city, date, weather, tem)
                    self.db.insert(city, date, weather, tem)
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)

    def process(self,cities):
        self.db = WeatherDB()
        self.db.openDB()
        for city in cities:
            self.forecasteWeather(city)

        self.db.closeDB()
        print("complete")


w = weatherForecast()
w.process(["深圳","广州"])










