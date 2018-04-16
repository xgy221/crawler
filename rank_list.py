import requests

url = "https://api.qimai.cn/app/comment?analysis=djBWVCwOVE93N2kEagEFBCFGSlQVFR4AXwheA1xCIxUBUwJSUlwPAQFXcBcC&appid=989673964&country=cn"
re1 = requests.get(url)


print(re1.json())


'''with open("rank_list.csv", "w", newline="") as w:
    for i in hjson.get('ret').get('ranks'):
        # print(str(i.get('rank'))+":"+str(i.get('game_name')))
        writer = csv.writer(w, delimiter='\t')
        writer.writerow(str(i.get('game_id')) + ',' + str(i.get('game_name')))'''


