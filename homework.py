import urllib.request as req   #我們用ullib模組
url='https://nidss.cdc.gov.tw/ch/NIDSS_DiseaseMap.aspx?dc=1&dt=5&disease=19CoV&fbclid=IwAR1RheO5u6OEteV-PNs_EvWgaLq-IvgvwkIHhf2lncmtp0ffbapSrsPejJo'
#將網址放在url的變數
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36" #由於我們要一直抓取資料，避免被系統認為我們是惡意程式，因此我們必須告訴網站我們是誰。
})

with req.urlopen(url) as response:
    data=response.read().decode("utf-8")#這裡是將url以uf8以中文呈現
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("td",align='center')
str1=str(titles)
import re
ste = re.sub("[A-Za-z\!\%\[\]\。\<\>\"\=\/\,]", "", str1)
sick=list(map(str, ste.split()))

import csv

city =['台北市','台中市','台南市','高雄市','基隆市','新竹市','嘉義市','新北市','桃園市','新竹縣','宜蘭縣','苗栗縣','彰化縣','南投縣','雲林縣','嘉義縣','屏東縣','澎湖縣','花蓮縣','台東縣','金門縣','連江縣']


with open('covid19.csv','w', newline='') as csvfile:

     fieldnames = ['縣市別','病例數']

     thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

     thewriter.writeheader()

     for i in range(0,22):
        thewriter.writerow({'縣市別':city[i],'病例數':sick[i]})
print('資料已存入excel')

