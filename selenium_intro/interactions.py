from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "C:/Users/Office/Desktop/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_tag_name("button")

first_name.send_keys("abc")
last_name.send_keys("pqr")
email.send_keys("xyz@email.com")
button.click()
# driver.quit()
