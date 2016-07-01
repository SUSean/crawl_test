import requests
from bs4 import BeautifulSoup
import lxml
import sys

#印出
def printHtml(tag) :
	for item in tag :
		print(item.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
payload = {'w': 'test'}
res = requests.post("http://yun.dreye.com/dict_new/dict.php", data=payload)

#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')

#印出網頁內容
#print(soup.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)) 

#使用select選取特定元素
tag = soup.select('#display_word span')
printHtml(tag)
tag = soup.select('#digest')
printHtml(tag)
tag = soup.select('#usual .sg')
printHtml(tag)
tag = soup.select('#usual .phrase')
printHtml(tag)
tag = soup.select('#usual .der')
printHtml(tag)
tag = soup.select('#usual .dif')
printHtml(tag)
