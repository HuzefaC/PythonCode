from selenium import webdriver

chrome_driver_path = "C:/Users/Office/Desktop/ChromeDriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
upcoming_events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
data = upcoming_events.text.split("\n")
my_dict = {}

for i in range(int(len(data)/2)):
    my_dict[i] = {
        "time": data[i],
        "name": data[i+1],  
    }

print(my_dict)
driver.quit()
