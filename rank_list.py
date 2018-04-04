import urllib.request

url = "http://fsight.qq.com/GameList?type=hotRank"
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode('utf-8')
print(html)