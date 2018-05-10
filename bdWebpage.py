import requests
from bs4 import BeautifulSoup
from datetime import datetime
import url2io
time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
url='你想搜什么就搜什么'
web_data=requests.get(url)
soup=BeautifulSoup(web_data.text,'html.parser')
for i in range(1,20):
    alink=soup.select('h3')[i].select('a')[0]['href']
    api = url2io.API('bjb4w0WATrG7Lt6PVx_TrQ')
    ret = api.article(url=alink, fields=['text', 'next'])
    text = ret['text']
    result = open('', 'a')#自己修改
    result.write(text)


