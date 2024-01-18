from bs4 import BeautifulSoup
import requests
import re
import unicodedata


class GoogleResult:
    def __init__(self):
        self.name = None
        self.link = None
        self.description = None

def GoogleSearchKiet(question):
    param = {"q": question}
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
    }
    r = requests.get("https://google.com/search", params=param, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    soup.prettify()
    #debug
    # with open("output1.html", "w", encoding='utf-8') as file:
    #     file.write(str(soup))

    listall = soup.findAll('div', {'class','Gx5Zad fP1Qef xpd EtOod pkphOe'})    
    result = []

    for liItem in listall:
   
        try:
            obj = GoogleResult()
            obj.link =  liItem.find('a')['href']
            if obj.link.startswith("/search?"):
                continue
            obj.name = liItem.find('h3',{'class','zBAuLc l97dzf'}).text
           
            obj.description = liItem.find('div',{'class','BNeawe s3v9rd AP7Wnd'}).text
          
            
            result.append(obj)
        except Exception as e :
            print(e)
    return result
    
    
question = "vụ tấn công ở đắk lắk"

a = GoogleSearchKiet(question)

for i in range(len(a)):
    print("Tiêu đề : ",a[i].name)
    print("Link : ", a[i].link)
    print("Mô tả : ",a[i].description)
    print("___________________________________")
