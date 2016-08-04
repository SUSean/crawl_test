import requests
from bs4 import BeautifulSoup
import lxml
import sys
import os

#印出
def getUrls(tag) :
	url = []
	for item in tag :
		id = item.get('id')
		if id[:12] == "normalthread":
			url.append("http://oursogo.com/thread"+"-"+id[13:]+"-1-1.html")
	return url

def printHtml(tag) :
	for item in tag :
		print(item.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

def saveImg(tag,dirName) :
	num = 1
	error_num = 0
	if not os.path.exists('pictures\\'+dirName) :
		try:
			os.mkdir('pictures\\'+dirName)
		except OSError :
			while True :
				error_num = error_num+1
				dirName = 'errorName'+str(error_num)
				if not os.path.exists('pictures\\'+dirName) :
					os.mkdir('pictures\\'+dirName)
					break
	else :
		return 
	for item in tag :
		if(item.get('file')) :
			url=item.get('file')
		else :
			url=item.get('src')
		print(url)
		with open('pictures\\'+dirName+'\\'+str(num)+'.jpg','wb') as f:
			r = requests.get(url)
			f.write(r.content)
			num=num+1

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
res = requests.get("http://oursogo.com/forum.php?mod=forumdisplay&fid=276&orderby=&page=1")
#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')
tag = soup.select('tbody')
urls = getUrls(tag)
for url in urls :
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	tag = soup.select('#thread_subject')
	printHtml(tag)
	name = tag[0].text
	tag = soup.select('ignore_js_op img')
	saveImg(tag,name)
	tag = soup.select('.vwmy')
	printHtml(tag)


