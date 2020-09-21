from datetime import datetime, timezone, timedelta

import pandas as pd
import numpy as np

import selenium
from selenium import webdriver

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from urllib.parse import quote_plus

import time
from tqdm import tqdm_notebook
from konlpy.tag import *
import warnings

warnings.filterwarnings('ignore')
okt = Okt()


def main_search(keyword):
    driver.get(url)
    assert "Google" in driver.title

    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.clear()
    search.send_keys(keyword)
    search_list1 = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
    search_list1.click()


def scroll_page():
    post_link.clear()
    popularPost_len.clear()
    while True:
        pageString = driver.page_source  # page_source : 현재 렌더링된 페이지의 Elements를 모두 가져옴
        bsObj = bs(pageString, 'lxml')

        for postline in bsObj.find_all(name='div', attrs={"class": "Nnq7C weEfm"}):
            a_len = len(postline.select('a'))
            popularPost_len.append(a_len)
            # 인스타그램 게시물은 행별로 최대 3개까지 확인할 수 있는데, 최근게시물이나 마지막 게시물은 1,2개가 나올 수도 있어서 len 지정
            for post in range(a_len):
                item = postline.select('a')[post]
                link = item.attrs['href']
                if link not in post_link:  # 스크롤을 내리고 중복된 것을 제거하지 않고 누적시키기 때문에 없는 것만 추가
                    post_link.append(link)

        last_height = driver.execute_script('return document.body.scrollHeight')  # 자바스크림트로 스크롤 길이를 넘겨줌
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # selenium에서 scroll 기능 사용
        time.sleep(SCROLL_PAUSE_TIME)
        # 프로세스 자체를 지정시간동안 기다려줌(무조건 지연)
        # driver.implicitly_wait(SCROLL_PAUSE_TIME)
        # 브라우저 엔진에서 파싱되는 시간을 기다려줌(요소가 존재하면 지연없이 코드 실행)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            # driver.implicitly_wait(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue


def popularPostSum():
    popularPost = 0
    for i in range(3):
        popularPost += popularPost_len[i]
    return popularPost


# 인기게시물은 시간순으로 나타나는 것이 아니므로
# 여기에 나타나는 항목들은 시간순으로 데이터프레임 만다는 데서 제외시키기 위한 함수​

def to_timestamp(std_date):
    date_string = std_date
    date = datetime.strptime(date_string, "%Y.%m.%d")
    time_tuple = date.timetuple()
    std_timestamp = time.mktime(time_tuple)
    return int(std_timestamp)


def date_based_crawling(std_date):
    id_list.clear()
    like_list.clear()
    tag_list.clear()
    link_list.clear()
    date_list.clear()
    month_list.clear()
    day_list.clear()
    content_list.clear()

    post_linkx = post_link[popularPostSum():]  # 스크롤 내리면서 모은 데이터 중 인기 게시물은 제외시킴
    num_of_postx = len(post_linkx)

    std_timestamp = to_timestamp(std_date)
    # 기준 날짜를 지나면 크롤링이 멈추도록 작동

    for i in tqdm_notebook(range(num_of_postx)):
        req = Request("https://www.instagram.com" + post_linkx[i], headers={'User-Agent': 'Mozila/5.0'})
        postpage = urlopen(req).read()

        post_body = bs(postpage, 'lxml', from_encoding='utf-8')
        post_core = post_body.find('meta', attrs={'property': "og:description"})
        contents = post_core['content']
        # print(contents)

        # break할 시간 비교
        posttxt = str(postpage)
        timestamp = int(posttxt[posttxt.find('taken_at_timestamp') + 20: posttxt.find('taken_at_timestamp') + 30])
        # print(date_list[-1][:9])

        if (std_timestamp > timestamp) and (to_timestamp(date_list[-1][:10]) - timestamp) > 86400:
            pass
        if (std_timestamp > timestamp) and (to_timestamp(date_list[-1][:10]) - timestamp) < 86400:
            break
        # 게시글 중간에 오래된 게시글이 올라오는 경우가 있어서 이전 게시글과 하루 이상 차이(timestamp 86400)가 나면
        # outlier로 간주하고 pass

        # 시간
        date_list.append(datetime.fromtimestamp(timestamp).strftime('%Y.%m.%d %H:%M'))
        month_list.append(datetime.fromtimestamp(timestamp).strftime("%m"))
        day_list.append(datetime.fromtimestamp(timestamp).strftime("%d"))

        # 개별 링크 리스트
        link_list.append("https://www.instagram.com" + post_linkx[i])

        # 좋아요
        try:
            likes = int(contents[: contents.find(' Likes, ')])  # Likes 문자열 앞에 있는 좋아요 개수 추출
        except:
            likes = 0  # 좋아요 가 아니라 조회수로 표시되는 경우도 있어 이런 경우는 0으로 표시
        like_list.append(likes)

        # 개별 계정
        if "@" and ")" in contents:
            personal_id = contents[contents.find("@") + 1: contents.find(")")]
        elif "shared a post on Instagram" in contents:
            personal_id = contents[contents.find("@") + 1: contents.find('shared a post on Instagram')]
        elif "shared a photo on Instagram" in contents:
            personal_id = contents[contents.find("@") + 1: contents.find('shared a photo on Instagram')]
        elif "@" and ")" not in contents and "on Instagram" in contents:
            personal_id = contents[contents.find("@") + 1: contents.find('on Instagram')]

        else:
            personal_id = contents[1: contents.find(' posted on')]
        id_list.append(personal_id)

        '''    
        (@personal_id) on instagram, @persoanlid posted on instagram, personal_id on instgram 등의 형태로 meta 데이터에 표시되기
        때문에 여러 형식별 id 추출 if문 수행
        '''

        # 해시태그
        tag_list.append([])
        for tag_content in post_body.find_all('meta', attrs={'property': "instapp:hashtags"}):
            hashtags = tag_content['content'].rstrip(',')
            tag_list[i].append(hashtags)

        # 본문내용
        content_list.append([])
        try:  # 여러 태그중 첫번째([0]) 태그를 선택
            content = contents[contents.find(":") + 1:]
            content_list[i].append(okt.morphs(content))
            # 첫 게시글 본문 내용이 <div class="C4VMK"> 임을 알 수 있다.
            # 태그명이 div, class명이 C4VMK인 태그 아래에 있는 span 태그를 모두 선택.
        except:
            content = ' '

SCROLL_PAUSE_TIME = 1.0
post_link = []
popularPost_len = []
id_list = []
like_list = []
tag_list = []
link_list = []
date_list = []
month_list = []
day_list = []
content_list = []

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR")
url = 'https://map.naver.com/v5/search/'
path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path, chrome_options=options)

# user_agent = driver.find_element_by_css_selector('#user-agent').text
# plugins_length = driver.find_element_by_css_selector('#plugins-length').text
# languages = driver.find_element_by_css_selector('#languages').text
#
# print('User-Agent: ', user_agent)
# print('Plugin length: ', plugins_length)
# print('languages: ', languages)

main_search('코로나')
scroll_page()
date_based_crawling("2020.09.10")
num_of_post = len(post_link)

print('총 {0}개의 게시글을 수집합니다.'.format(num_of_post))

insta_dict = {'날짜': date_list,
              # '월': month_list,
              # '일': day_list,
              # '계정': id_list,
              '좋아요': like_list,
              '해시태그': tag_list,
              '링크': link_list,
              '내용': content_list
              }
df = pd.DataFrame(content_list)
df.to_csv('review.csv', mode='w', encoding='utf-8', header=None)
driver.quit()
