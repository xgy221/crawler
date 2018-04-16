import urllib.request
import json
import csv

url = "http://fsight.qq.com/GameListAjax"
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode('utf-8')
print(html)
hjson = json.loads(html)
# print(hjson)
with open("rank_list.csv", "w", newline="") as w:
    for i in hjson.get('ret').get('ranks'):
        # print(str(i.get('rank'))+":"+str(i.get('game_name')))
        writer = csv.writer(w, delimiter='\t')
        writer.writerow(str(i.get('game_id')) + ',' + str(i.get('game_name')))


