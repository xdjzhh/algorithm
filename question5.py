'''这个题我不太理解，是从网页上筛选有用信息还是已知多个文件筛选具有Max Lynch信息的文件？？？
'''
import bs4
import re
import json
import urllib.request
import time
from selenium import webdriver

#网页爬取相关信息，如果只是个人信息与比赛详情感觉并没有必要进行爬取

'''由于谷歌反爬虫太牛皮 所以用selenium操作 限定chrome版本75.0'''
url = 'https://www.google.com/search?q=Max+Lynch&oq=Max+Lynch&aqs=chrome..69i57j35i39j0l4.7735j0j8&sourceid=chrome&ie=UTF-8'
driver = webdriver.Firefox()
driver.get(url)
content = driver.page_source.encode('utf-8')
soup = bs4.BeautifulSoup(content, "html.parser")
content_list = soup.find(name='div',attrs={'class':'srg'}).find_all(name='div',attrs={'class':'g'})
url_list = []
for i in content_list:
    i.find(name='div',attrs={'class':'r'}).get('href')


def get_url_content(url):
    file = urllib.request.urlopen(url)
    file.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Chrome/75.0')]
    content = file.read().decode('utf-8')
    soup = bs4.BeautifulSoup(content, "html.parser")
    return soup


def get_content(url):
    soup = get_url_content(url)
    print(soup)
    '''现在可以对url进行各种筛选'''
    url_list = soup.find()
    print(url_list)
    '''并利用driver的功能进行点击操作'''
    driver.find_element_by_xpath('//button[@class="a-browse-more-controls-btn"][@data-type="Program"]').click()

    '''当页面变换时，通过标签选定相关内容   或者  直接利用str()的方式将页面字符串化，然后用re.sub()对无关的信息进行筛选'''
    content = driver.page_source.encode('utf-8')
    soup = bs4.BeautifulSoup(content, "html.parser")
    all_text = re.sub(r'pattern',str(soup))


#相关文件搜索，若给出无数文件，寻找相关的top10 文件可以用tfidf(idf没变，所以决定于tf，tf决定于搜索的单词个数，所以直接计算个数)
# 进行操作，若是提前做好索引的文件就更为简单，若为搜索一句话的相关性可以用sklearn.feature_extraction.text库的 TfidfVectorizer
import os
def file_read(filepath):
    file_list = os.listdir(filepath)
    file_name = []
    for i in file_list:
        f = open(i)
        lines = f.read()
        content = re.sub('\n',' ',lines.lower())
        content = re.sub('max lynch','max_lynch')
        word_count = content.split(' ').count('Max Lynch')
        if word_count >0:
            file_name.append(i)
    return file_name