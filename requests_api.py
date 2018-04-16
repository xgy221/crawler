import requests
import csv

url1 = 'http://fsight.qq.com/GameList?type=hotRank'
url2 = 'http://fsight.qq.com/GameListAjax'
r1 = requests.get(url1)
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '53',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'wetest_crsftoken=2e855df53a3cf7a2ba4eb390d500ab4cfea782287c6cd7167ac8884153a48202a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22wetest_crsftoken%22%3Bi%3A1%3Bs%3A32%3A%22SB5ay7ROKlM1PBxRvmKtKUJZtvrlDHro%22%3B%7D; wetest_token=WWROVjM5QXcKJns3Sg4TOBIIA2djezklLwkFInhsCy0tEjw6d3EzGA%3D%3D; pgv_pvi=1046328320; pgv_si=s9362995200; country=0; Hm_lvt_7fda3007b2d4e4b63d3da08216838e5e=1523518894; Hm_lpvt_7fda3007b2d4e4b63d3da08216838e5e=1523518894; _qddaz=QD.7wgb9o.2m40e2.jfw7ta64; _qdda=3-1.1; _qddab=3-fnjgb3.jfw7ta65; _qddamta_800074165=3-0; tencentSig=9514326016; _qddac=3-2-1.1.fnjgb3.jfw7ta65',
    'Host': 'fsight.qq.com',
    'Origin': 'http://fsight.qq.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://fsight.qq.com/GameList?type=hotRank',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'X-BEE-COUNTRY': '0',
    'X-CSRF-TOKEN': 'WWROVjM5QXcKJns3Sg4TOBIIA2djezklLwkFInhsCy0tEjw6d3EzGA==',
    'X-Requested-With': 'XMLHttpRequest',
}

postData = {
    'listCat': 1,
    'listType': 0,
    'rankRange': 1,
    'listDate': "2018-02-02"
}

r2 = requests.post(url2, headers=headers, data=postData)
print("Status code:", r2.status_code)
print(r2.text)
