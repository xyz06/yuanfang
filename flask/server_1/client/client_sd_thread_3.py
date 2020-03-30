import urllib.request
from bs4 import BeautifulSoup
import threading


def downloadImg(url, fileName):
    try:                        # 设置下载时间最长100秒
        data = urllib.request.urlopen(url, timeout=100)
        data = data.read()
        fobj = open("download" + fileName, "wb")
        fobj.write(data)
        fobj.close()
        print("downloaded", fileName)
    except Exception as err:
        print(err)

#返回links列表
def visit(url):
    global urls
    if url in urls:
        return []
    urls.append(url)
    try:
        data = urllib.request.urlopen(url)
        data = data.read()
        data = data.decode()
        soup = BeautifulSoup(data, "html.parser")
        print(soup.find("title").text)
        links = soup.select("a")
        div = soup.select("div")
        img = soup.select("img")
        if len(div) > 0 and len(img) > 0:
            note = div[0].text
            print(note)
            url = start_url + "/" + img[0]["src"]
            img = img[0]["src"]
            # 启动线程用于下载图片
            T = threading.Thread(target=downloadImg, args=(url, img))
            T.setDaemon(False)
            T.start()
            threads.append(T)  # 把线程插入列表中

        return links
    except Exception as err:
        print(err)


def spider(url):
    links = visit(url)
    for link in links:
        href = link["href"]
        url = start_url + "/" + href
        spider(url)


start_url = "http://127.0.0.1:5000"
urls = []
threads = []
spider(start_url)

# 等待所有线程执行完毕
for t in threads:
    t.join()
print("The End")
