import urllib.request
import urllib.parse
import threading
from bs4 import UnicodeDammit
from bs4 import BeautifulSoup

def download(url,count):
    try:
        if(url[len(url)-4] == "."):  #地址最后第4个字符 是否为 "."
            ext = url[len(url)-4:]   #取图片后缀 .xxx
        else:
            ext = ""
        req = urllib.request.Request(url, headers=header)
        data = urllib.request.urlopen(req, timeout=100)
        data = data.read()
        file = open("../jvruimage/" + str(count) + ext, "wb")
        file.write(data)
        file.close()
        print("downloaded" + str(count) + ext)
    except Exception as err:
        print(err)


def spiderImage(url):
    global urls
    global count
    req = urllib.request.Request(url, headers=header) #伪装成浏览器
    data = urllib.request.urlopen(req)   #访问网站
    data = data.read()      #读取网站内容
    dammit = UnicodeDammit(data, ['utf-8', 'gbk'])
    data = dammit.unicode_markup
    soup = BeautifulSoup(data, "html.parser")
    imgs = soup.select("img")
    for img in imgs:
        try:
            src = img["src"]
            url = urllib.parse.urljoin(start_url, src)
            if url not in urls:
                urls.append(url)
                print(url)
                T = threading.Thread(target=download, args=[url,count])
                T.setDaemon(False)
                T.start()
                threads.append(T)
                count = count + 1
        except Exception as err:
             print(err)

#start_url = "https://www.jia.com/zx/shanghai/anli/524909_xiaoguo/"
start_url = "https://www.meitulu.com/item/19474.html"
#start_url = "http://www.weather.com.cn/weather/101280601.shtml"
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
}
count = 0
urls= []
threads = []
spiderImage(start_url)
for t in threads:
    t.join()
print("The End")
