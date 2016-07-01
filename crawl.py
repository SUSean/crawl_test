#coding=utf-8

import requests
from bs4 import BeautifulSoup
import lxml
import sys

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
res = requests.get("http://maplestage.com/")

#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')

#印出網頁內容
#print(soup.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)) 

#使用select選取特定元素
hrefs = soup.select('a')


#印出
for href in hrefs :
	text=str(href)
	print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))