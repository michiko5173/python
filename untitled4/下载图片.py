import requests,os,bs4
url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
#下载页面
    resAll=requests.get(url)
    soup = bs4.BeautifulSoup(resAll.text)
    #找到图片
    comicElem=soup.select('#comic img')
    comicUrl='http:'+comicElem[0].get('src')
    print(comicUrl)
    resComic=requests.get(comicUrl)
    #下载图片
    if resComic.status_code == 200:
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb').write(resComic.content)
    #下一页
    privLink = soup.select('a[rel=prev] ')
    url= 'http://xkcd.com'+privLink[0].get('href')