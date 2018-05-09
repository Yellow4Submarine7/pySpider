from bs4 import BeautifulSoup
import urllib
import requests
import urllib.request
import urllib.parse
import url2io
word = '你想搜什么就搜什么'
key = urllib.parse.quote(word)
url = 'http://www.baidu.com.cn/s?wd=' + key + '&pn=0'
response = urllib.request.urlopen(url)
page = response.read()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}
all = open('/Users/cunter/Desktop/爬虫/test.txt', 'a')
soup = BeautifulSoup(page,'lxml')
tagh3 = soup.find_all('h3')
for h3 in tagh3:
    href = h3.find('a').get('href')
    baidu_url = requests.get(url=href, headers=headers, allow_redirects = False)
    real_url = baidu_url.headers['Location']
    if real_url.startswith('http'):
        all.write(real_url + '\n')
        api = url2io.API('bjb4w0WATrG7Lt6PVx_TrQ')
        ret = api.article(url=real_url,fields=['text', 'next'])
        text = ret['text']
        result = open('/Users/cunter/Desktop/爬虫/result.txt','a')
        result.write(text)


