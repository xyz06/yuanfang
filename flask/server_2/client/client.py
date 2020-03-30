from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#设置浏览器不可见
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#driver= webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()  #创建一个浏览器
driver.get("http://127.0.0.1:5000")  #浏览器访问该网址

#html = driver.page_source   获取网站页面内容

#soup = BeautifulSoup(html, "html.parser")
#hmsg = soup.find("span",attrs={'id':"hmsg"}).text
#print(html)
#print(hmsg)

#获取标签中的文本
elem =driver.find_element_by_xpath("//div[@class='phone']//p[@class='price']").text
print(elem)

elem =driver.find_element_by_xpath("//div[@class='phone']//p[@class='price']")
cl = elem.get_attribute("class")  #获取标签中的属性
print(cl)

#获取标签id
print(driver.find_element_by_id("hmsg").text)


try:
    a = driver.find_element_by_link_text("联通通讯") #查找a标签文本为“联通通讯”
    print(a.text)
    b = driver.find_element_by_partial_link_text("联通")   #模糊查找 a标签
    c = driver.find_element_by_class_name("phone")
    print(b.text,b.get_attribute("href"))
    print(c.text)
except:
    pass


try:
    print(driver.current_url)  #显示当前网页地址
    u = driver.find_element_by_name("user")
    p = driver.find_element_by_name("pwd")
    l = driver.find_element_by_name("login")
    u.send_keys("xyz")    #在表单用户名填入 xyz
    p.send_keys("123")    #在表当密码 填入123
    l.click()
except:
    pass


#爬取table中的数据
print(driver.current_url)
trs = driver.find_elements_by_tag_name("tr")
for i in range(1,len(trs)):
    tds = trs[i].find_elements_by_tag_name("td")
    if len(tds)==3:
        model = tds[0].text
        mark = tds[1].text
        price =tds[2].text
        print("%-16s %-16s %-16s" % (model, mark, price))




driver.close()



