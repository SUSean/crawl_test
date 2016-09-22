import requests
from bs4 import BeautifulSoup
import lxml
import sys
import os

def printHtml(tag) :
	for item in tag :
		print(item.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

def addWords(tag) :
	words={}
	for item in tag :
		words[item.text]=item.get('href')
	print(words)

while True :
	s=requests.session()
	word = input("請輸入Word：")
	if word == "kill" :
		break
	payload = {'w': word}
	#res = s.get("http://yun.dreye.com/dict_new/dict.php", params=payload)
	res = s.post("http://yun.dreye.com/dict_new/dict.php",data=payload)
	soup = BeautifulSoup(res.text,'lxml')
	tag = soup.select('.content')
	printHtml(tag)
	tag = soup.select('.ews_sys_msg a')
	addWords(tag)


