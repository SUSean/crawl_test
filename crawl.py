import requests
from bs4 import BeautifulSoup
import lxml
import sys
import os

#印出
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
	for item in tag :
		if(item.get('file')) :
			url=item.get('file')
		else :
			url=item.get('src')
		print(url)
		with open('pictures\\'+dirName+'\\'+str(num).zfill(3)+'.jpg','wb') as f:
			r = requests.get(url)
			f.write(r.content)
			num=num+1


url = input('請輸入URL：')
payload = {'answer':'','loginsubmit':'true','password':'080000','questionid':'0','username':'SUSean'}
s=requests.session()
res=s.post(url='http://oursogo.com/member.php?mod=logging&action=login',data=payload)

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
#payload = {'w': 'test'}
#res = requests.post("http://yun.dreye.com/dict_new/dict.php", data=payload)
#res = requests.get("http://yun.dreye.com/dict_new/dict.php", params=payload)
res = s.get(url)
#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')

#印出網頁內容
#print(soup.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)) 

#使用select選取特定元素
tag = soup.select('#thread_subject')
printHtml(tag)
name = tag[0].text
tag = soup.select('ignore_js_op img')
tag = tag+soup.select('.showhide a img')
saveImg(tag,name)
tag = soup.select('.vwmy')
printHtml(tag)
