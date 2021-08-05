import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
def security_news():
  headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept-Language':'ko-KR,ko'} # 한글페이지 반환
  # 헤더를 명시안하면 크롬의 영어버전(디폴트) 기준으로 반환됨.
  
  file=open("./Security_news.json","w",encoding="utf-8")
  result_array = []
  date = int(datetime.today().strftime('%Y%m%d'))

  for i in range(1, 4):
    security_news_url = f'https://www.wired.com/category/security/page/{i}/'
    print('page = ', i)
    print(security_news_url)
    res = requests.get(security_news_url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    itnews = soup.find('ul', attrs = {'class':'archive-list-component__items'}).find_all('li')
    links = soup.find('a', sttrs  = {'class':'archive-item-component__link'})

    for index, news in enumerate(itnews):
      news_date = news.find('div', attrs = {'archive-item-component__byline'}).find('time').get_text()
      title = news.find('h2', attrs = {'archive-item-component__title'}).get_text().strip()
      link = 'https://www.wired.com' + news.find('a', attrs = {'archive-item-component__link'})['href']
      print(index+1)
      print(news_date)
      print(title)
      print(link)
      result={"date":news_date, "id": index, "title":title,"링크":link}
      result_array.append(result)
    print()
    
  file.write(json.dumps(result_array, ensure_ascii=False,indent=2))
  file.close()

security_news()