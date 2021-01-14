from selenium import webdriver

chrome_driver_path = "C:/Users/Office/Desktop/ChromeDriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.in")

driver.quit()
