from bs4 import BeautifulSoup
import requests as req
import pandas as pd


print('Starting Task...')

url = 'https://comic.naver.com/webtoon/weekdayList?week=thu'
res = req.get(url)
soup = BeautifulSoup(res.content, 'lxml')

names = soup.select('#content > div.list_area.daily_img > ul > li > dl > dt > a')
writers = soup.select('#content > div.list_area.daily_img > ul > li > dl > dd.desc > a')
rates = soup.select('#content > div.list_area.daily_img > ul > li > dl > dd:nth-child(3) > div > strong')

list_names = [name.text for name in names]
list_writers = [writer.text for writer in writers]
list_rates = [rate.text for rate in rates]

df_cartoon = pd.DataFrame(data={'Names':list_names, 'Writers':list_writers, 'rates':list_rates})

df_cartoon.to_csv('webtoon_crawler.csv')
print('Task Done!')