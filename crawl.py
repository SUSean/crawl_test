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
	if not os.path.exists(dirName) :
		os.mkdir(dirName)
	for item in tag :
		if(item.get('file')) :
			url=item.get('file')
		else :
			uel=item.get('src')
		print(url)
		with open(dirName+'\\'+str(num)+'.jpg','wb') as f:
			r = requests.get(url)
			f.write(r.content)
			num=num+1

url = input('請輸入URL：')
payload = {'answer':'','formhash':'beba44d9','loginsubmit':'true','password':'080000','questionid':'0','referer':'http://oursogo.com/','username':'SUSean'}
s=requests.session()
s.post(url='http://oursogo.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LLb3D&inajax=1'
	,data=payload)
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
saveImg(tag,name)
tag = soup.select('.vwmy')
printHtml(tag)
tag = soup.select('#thread_subject')
printHtml(tag)
