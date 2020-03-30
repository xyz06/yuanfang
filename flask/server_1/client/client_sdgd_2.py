from bs4 import BeautifulSoup
import urllib.request

class Stack:
    def __init__(self):
        self.s = []

    def push(self,obj):
        self.s.append(obj)

    def pop(self):
     #   return self.s.pop() #1 深度
        return self.s.pop(0) #2 广度

    def empty(self):
        return len(self.s) == 0


def spider(url):
    global urls
    st = Stack()
    st.push(url)
    while not st.empty():
        url = st.pop()
        if url not in urls:
            try:
                urls.append(url)
                data = urllib.request.urlopen(url) #访问网站
                data = data.read() #读取网站内容
                data = data.decode() #解码网站
                soup = BeautifulSoup(data, "html.parser")
                print(soup.find("title").text)
                links = soup.select("a")
            #1深度
            #    for i in range(len(links)-1, -1, -1):
            #       href = links[i]["href"]
            #       url = start_url + "/" + href
            #       st.push(url)
            #2广度
                for link in links:
                   href = link["href"]
                   url = start_url + "/" + href
                   st.push(url)

            except Exception as err:
                print(err)

start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print('The End')