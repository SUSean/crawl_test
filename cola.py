import requests
from bs4 import BeautifulSoup
import lxml
import sys
import os

#印出
def getUrls(tag) :
	url = []
	for item in tag :
		id = item.get('href')
		if id == None :
			continue
		else :
			url.append(id)
	return url

def printHtml(tag) :
	for item in tag :
		print(item.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

def saveImg(tag,dirName) :
	num = 1
	error_num = 0
	if not os.path.exists('cola\\'+dirName) :
		try:
			os.mkdir('cola\\'+dirName)
		except OSError :
			while True :
				error_num = error_num+1
				dirName = 'errorName'+str(error_num)
				if not os.path.exists('cola\\'+dirName) :
					os.mkdir('cola\\'+dirName)
					break
	else :
		return 
	for item in tag :
		url=item.get('src')
		print(url)
		with open('cola\\'+dirName+'\\'+str(num).zfill(3)+'.jpg','wb') as f:
			r = requests.get(url)
			f.write(r.content)
			num=num+1


s=requests.session()
#res=s.post(url='http://oursogo.com/member.php?mod=logging&action=login',data=payload)
res = s.get("http://colapic.com/category/meinv/")

#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')

tag = soup.select('.excerpt h2 a')
urls = getUrls(tag)
for url in urls :
	res = s.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	tag = soup.select('.article-title')
	printHtml(tag)
	name = tag[0].text
	tag = soup.select('.article-content img')
	saveImg(tag,name)


