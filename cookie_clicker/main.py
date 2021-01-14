from selenium import webdriver
import time
chrome_driver_path = "C:/Users/Office/Desktop/ChromeDriver/chromedriver.exe"
URL = "https://orteil.dashnet.org/cookieclicker/"

BONUS_XPATHS = {
    '15': '//*[@id="buyCursor"]',
    '100': '//*[@id="buyGrandma"]',
    '500': '//*[@id="buyFactory"]',
    '2000': '//*[@id="buyMine"]',
    '7000': '//*[@id="buyShipment"]',
    '50000': '//*[@id="buyAlchemy lab"]',
    '1000000': '//*[@id="buyPortal"]',
    '123456789': '//*[@id="buyTime machine"]'
}

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')


def get_higher_bonus():
    higher_key = '0'
    count = driver.find_element_by_id('money').text
    for key, value in BONUS_XPATHS.items():
        if int(higher_key) < int(key) < int(count):
            higher_key = key
    driver.find_element_by_xpath(BONUS_XPATHS[higher_key]).click()


start_time = time.time()
bonus_time_counter = start_time

while time.time() - start_time < 299:
    cookie.click()
    if time.time() - bonus_time_counter > 5:
        bonus_time_counter = time.time()
        get_higher_bonus()
