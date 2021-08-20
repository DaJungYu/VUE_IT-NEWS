import enum
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def parse_itnews(itnews_headline, itnews, i):
    result_array=[]
    for index, news in enumerate(itnews_headline):
        result={}
        a_inx=0
        img=news.find("img")
        if img:
            a_inx=1 #img 태그가 있으면 1번째 a 태그의 정보를 사용
            
        title=news.find_all("a")[a_inx].get_text().strip()
        description=news.find("dd").find("span","lede").get_text().strip()
        link= news.find_all("a")[a_inx]["href"]
        print("{}. {}".format(index+1,title))
        print("{}".format(description))
        print("  (링크 : {})".format(link))
        #result={"{}. {}".format(index+1,title)," (링크 : {})".format(link)}

        result={"id": index+1,"date":datetime.strptime(str(i),'%Y%m%d').strftime('%Y-%m-%d'), "title":title,"description":description,"link":link}
        result_array.append(result)

    if itnews == None:
        return result_array

    for index, news in enumerate(itnews):
        result={}
        a_inx=0
        img=news.find("img")
        if img:
            a_inx=1 #img 태그가 있으면 1번째 a 태그의 정보를 사용
            
        title=news.find_all("a")[a_inx].get_text().strip()
        description=news.find("dd").find("span","lede").get_text().strip()
        link= news.find_all("a")[a_inx]["href"]
        print("{}. {}".format(index+11,title))
        print("{}".format(description))
        print("  (링크 : {})".format(link))
        #result={"{}. {}".format(index+1,title)," (링크 : {})".format(link)}

        result={"id": index+11,"date":datetime.strptime(str(i),'%Y%m%d').strftime('%Y-%m-%d'), "title":title, "description":description, "link":link}
        result_array.append(result)

    return result_array

# ========= [Naver IT News] ==========
def naver_news():
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} # 한글페이지 반환

    file=open("./news.json","w",encoding="utf-8")
    date=int(datetime.today().strftime('%Y%m%d'))
    result_array = []

    for i in range(date,date-5,-1):
        pagenum = 1
        while 1:
            naver_news_url=f'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=732&sid1=105&date={i}&page={pagenum}'
            print('date=',i)
            print(naver_news_url)
            res = requests.get(naver_news_url, headers = headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')

            itnews_headline=soup.find('ul',attrs={'class':'type06_headline'}).find_all('li')
            itnews=soup.find('ul',attrs={'class':'type06'})
            itnews_span_tag=soup.find('span',attrs={'class':'lede'})
            if itnews != None:
                itnews = itnews.find_all('li')

            result_array.extend(parse_itnews(itnews_headline, itnews, i))

           
            itnews_a_tag=soup.find('div',attrs={'class':'paging'}).find_all("a") # findall로 a태그를 전부 가져온다
            if itnews_a_tag == None: # 페이지 없을때 None 나오는지 체크
                break

            status = False

            for page in itnews_a_tag:
                number=int(page.get_text())
                # print(pages)
                if number > pagenum:
                    status = True
                    pagenum=pagenum+1
                    break


            # itnews_span_tag=soup.find('span',attrs={'class':'lede'})
            # if itnews_span_tag==None:
            #     break
            # status=False

            # for page in itnews_span_tag:
            #     number=int(page.get_text())
            #     if number > pagenum:
            #         status = True
            #         pagenum=pagenum+1
            #         break

            if status:
                continue
            else:
                break

            
            
            # itnews_a_tag를 for문 돌려서 모든 a태그의 내용(페이지 숫자)을 보면서
            # pagenum 보다 큰 게 있으면 -> pagenum 업데이트 하고 continue

            # paging의 a태그의 text를 뽑아서 이 다음 페이지의 링크가 있는지 본다
            # 링크가 없으면 break해서 while 1 탈출
            



    file.write(json.dumps(result_array, ensure_ascii=False,indent=2))
    file.close()
    print()
naver_news()

# def print_news():
#     for index, news in enumerate(itnews_headline):
#         result={}
#         a_inx=0
#         img=news.find("img")
#         if img:
#             a_inx=1 #img 태그가 있으면 1번째 a 태그의 정보를 사용
            
#         title=news.find_all("a")[a_inx].get_text().strip()
#         link= news.find_all("a")[a_inx]["href"]
#         print("{}. {}".format(index+1,title))
#         print("  (링크 : {})".format(link))
#         #result={"{}. {}".format(index+1,title)," (링크 : {})".format(link)}

#         result={"date":i,f"title{[index+1]}":title,"link":link}
#         result_array.append(result)



