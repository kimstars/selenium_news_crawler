from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
from unidecode import unidecode

def initDriver():

    WINDOW_SIZE = "1000,2000"
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-gpu') if os.name == 'nt' else None  # Windows workaround
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-feature=IsolateOrigins,site-per-process")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--ignore-certificate-error-spki-list")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-blink-features=AutomationControllered")
    chrome_options.add_experimental_option('useAutomationExtension', False)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")  # open Browser in maximized mode
    chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_argument('disable-infobars')

    driver = webdriver.Chrome(options=chrome_options)
    return driver



class GoogleResult:
    def __init__(self):
        self.name = None
        self.link = None
        self.description = None
    def show(self):
        print("link : ",self.link)
        print("name : ",self.name)
        print("description : ",self.description)
    def returnjson(self):
        return {"name":self.name,
                "link":self.link,
                "description":self.description
                }
        
def get_info(item):
    obj = GoogleResult()
    
    try:
        obj = GoogleResult()
        obj.link =  item.find('a')['href']
        obj.name = item.find('div',{'class','n0jPhd ynAwRc MBeuO nDgy9d'}).text
        obj.time = item.find('div',{'class','OSrXXb rbYSKb LfVVr'}).text
        obj.description = item.find('div',{'class','GI74Re nDgy9d'}).text
        
    except Exception as e :
        print(e)
    
    print("\n________________________________________________\n")
    obj.show()
    return obj





driver = initDriver()
from selenium.webdriver.common.keys import Keys
keyword = "vụ tấn công ở đắk lắk"
keyword = "tổng bí thư trung quốc đến thăm việt nam"
driver.get("https://www.google.com/search?sca_esv=599503376&sxsrf=ACQVn0-YkRlT1UNLhRnMzK7gcVba-gwsLQ:1705596004849&tbm=nws&q="+keyword)


#caodulieu va chuyen trang
data = []
for _ in range(10):
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')

    listall = soup.findAll('div', {'class','SoaBEf'})    

    for item in listall:
        temp = get_info(item)
        data.append(temp.returnjson())
        
    url = soup.find_all('td',{'class','d6cvqb BBwThe'})[1].find('a')['href']
    driver.get("https://www.google.com/"+url)
    
    
fileoutput = unidecode(keyword).replace(" ","_")

print(fileoutput)
