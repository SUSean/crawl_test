import requests
from bs4 import BeautifulSoup
import lxml
import sys
import os

payload = {'answer':'','loginsubmit':'true','password':'080000','questionid':'0','username':'SUSean'}

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
s=requests.session()
res=s.post(url='http://oursogo.com/member.php?mod=logging&action=login',data=payload)
#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')

#印出網頁內容
print(soup.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)) 


