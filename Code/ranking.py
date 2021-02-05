# 爬取2021-QS世界大学综合排名

from bs4 import BeautifulSoup
import requests
import re
import csv


url = 'https://www.compassedu.hk/qs'
html = requests.get(url)
html.encoding = 'utf-8'
list=[]
bs_html = BeautifulSoup(html.text, 'html.parser')
trs = bs_html.find_all('tr', class_='odd')
for item in trs:
    ranking = item.findAll('td')[0].text
    name = item.findAll('td')[1].text
    country = item.findAll('td')[2].text
    dir = {"ranking": ranking, "name": name, "country": country}
    list.append(dir)

csvfile = open('ranking.csv', "w", newline='', encoding='utf-8')
writer = csv.writer(csvfile)
# 表头
writer.writerow(('排名', '学校名称', '国家'))
for item in list:
    writer.writerow([item['ranking'], item['name'], item['country']])
csvfile.close()

