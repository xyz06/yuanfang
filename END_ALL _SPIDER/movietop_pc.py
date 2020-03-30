from bs4 import BeautifulSoup
import bs4.element
import re
doc = '''
<ol class="grid_view">
<li>
            <div class="item">
                <div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/" class="">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>


                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.7</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1928541人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>      
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">2</em>
                    <a href="https://movie.douban.com/subject/1291546/">
                        <img width="100" alt="霸王别姬" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291546/" class="">
                            <span class="title">霸王别姬</span>
                                <span class="other">&nbsp;/&nbsp;再见，我的妾  /  Farewell My Concubine</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 陈凯歌 Kaige Chen&nbsp;&nbsp;&nbsp;主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br>
                            1993&nbsp;/&nbsp;中国大陆 中国香港&nbsp;/&nbsp;剧情 爱情 同性
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.6</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1418848人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">风华绝代。</span>
                            </p>
                        </div>
                 </div>
            </li>
    </ol>
  
<div class="paginator">
        <span class="prev">
            <link rel="prev" href="?start=25&amp;filter=">
            <a href="?start=25&amp;filter=">&lt;前页</a>
        </span>
        
        

                
            <a href="?start=0&amp;filter=">1</a>
        
                
            <a href="?start=25&amp;filter=">2</a>
        
                <span class="thispage">3</span>
                
            <a href="?start=75&amp;filter=">4</a>
        
                
            <a href="?start=100&amp;filter=">5</a>
        
                
            <a href="?start=125&amp;filter=">6</a>
        
                
            <a href="?start=150&amp;filter=">7</a>
        
                
            <a href="?start=175&amp;filter=">8</a>
        
                
            <a href="?start=200&amp;filter=">9</a>
        
                
            <a href="?start=225&amp;filter=">10</a>
        
        <span class="next">
            <link rel="next" href="?start=75&amp;filter=">
            <a href="?start=75&amp;filter=">后页&gt;</a>
        </span>

            <span class="count">(共250条)</span>
        </div>  
                  
'''
soup = BeautifulSoup(doc, "html.parser")
lis = soup.select("ol[class='grid_view'] li")
for li in lis:
    titles = li.select("div[class='hd'] a span")
    title = []
    for t in range(len(titles)):
        tt = titles[t].text.strip()
        title.append(tt)
    p = li.select("div[class='bd'] p")[0]


    res = []
    flag = True
    for c in p.children:
        #判断C是不是bs4.element.NavigableString类型,是不是字符串
        if isinstance(c, bs4.element.NavigableString):
            t = c.string.strip("\n").strip()
            if t!="":
                if flag:
                    pos = t.find("主演")
                    director = t[:pos].replace("导演:","")
                    actor = t[pos+3:]
                    res.append(director)
                    res.append(actor)
                else:
                    st = t.split("/")
                    for e in st:
                        res.append(e)
                    break
        #判断c是不是bs4.element.Tag类型，是不是标签  并且c标签为<br>
        elif isinstance(c,bs4.element.Tag) and c.name =="br":
            flag = False

    img = li.select("img")[0].get("src")
    rating_num = li.select("span[class='rating_num']")[0].text
    quote = li.select("span[class='inq']")[0].text
    #(img)
    print(rating_num,quote)
    print(img)


    #input()
    #rint(dy[:dy.find("主演")].replace("导演:",""))
    #m = re.search("主演",dy).start()
    #dao = dy[:m].strip()
    #e = re.search("导演:",dao).end()
    #dao = dao[e:]

next_page = soup.select("div[class='paginator'] span[class='next'] a")[0].get("href")
print(next_page)

input()
#lis = soup.find("ol").find_all("li")
for li in lis:
    info = li.find("div", atts={"class":"info"})
    print(info)
    hd = info.find("div", atts={'class':'hd'})

    titles = hd.find_all("span",attrs={'class':'title'})
    title = []
    for i in titles:
        title.append(i.text)
    print(title)
