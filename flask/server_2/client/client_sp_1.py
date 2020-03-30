from selenium import webdriver
import time

url = "http://127.0.0.1:5000"
driver = webdriver.Chrome()
driver.get(url)
user = driver.find_element_by_name("user")
pwd = driver.find_element_by_name("pwd")
btn = driver.find_element_by_name("login")
time.sleep(1)
user.send_keys("xyz")
time.sleep(2)
pwd.send_keys("123")
time.sleep(3)
btn.click()
print(driver.page_source)