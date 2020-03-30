from bs4 import BeautifulSoup
import urllib.request


class Stack:
    def __init__(self):
        self.s = []

    def push(self,obj):
        self.s.append(obj)

    def pop(self):
        return self.s.pop()  #广度 return self.s.pop(0)

    def empty(self):
        return len(self.s) == 0



def spider(url):
    st = Stack()
    st.push(url)  #先入栈
    while not st.empty():  #不为空
        url = st.pop()    #出栈
        try:
            data = urllib.request.urlopen(url)  #访问网站
            data = data.read()   #读取网站内容
            data = data.decode() #解码
            soup = BeautifulSoup(data, "html.parser")
            print(soup.find("title").text)  #找到标签<title>中的文本
            links = soup.select("a")
        #1 深度搜索
            for i in range(len(links)-1, -1, -1):  # 假定len(links)为4，i 依次为 3,2,1,0
                href = links[i]["href"]
                url = start_url + "/" + href
                st.push(url)
        #2 广度搜索
        #    for link in links:
        #       href = link["href"]
        #        url = start_url + "/" + href
        #       st.enter()
        except Exception as err:
            print(err)


start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print("The End")