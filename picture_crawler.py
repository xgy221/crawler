import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.png)" alt'
    imgre = re.compile(reg)
    html = html.decode('gb2312')
    imglist = re.findall(imgre, html)
    x = 10
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.png' % x)
        x += 1


html = getHtml("http://www.3lian.com/gif/2008/8-1/00130953823_2.html")

print(getImg(html))
