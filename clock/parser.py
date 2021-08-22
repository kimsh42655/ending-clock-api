import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clockproject.settings")
import django
django.setup()

from clock.models import Notice

def parse_notice():
    url = 'https://www.korea.ac.kr/cop/portalBoard/portalBoardList.do?siteId=university&type=NG&id=university_060201000000'
    req = requests.get(url)
    if req.status_code == 200:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select('#contents_body > div.sub_contents > div.datalist_type1.mb20 > ul > li > div.summary')
        data = {}
        for notice in notices:
            title = notice.select_one('a').text
            date = notice.select_one('ul > li:last-child > strong').text[6:]
            data[title] = date
        
        return data
    else :
        print(req.status_code)