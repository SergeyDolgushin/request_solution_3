from pprint import pprint
import requests
from datetime import timedelta, timezone, datetime


def input_date(todate = datetime.now(timezone.utc), interval = 2):
    """ввод начальной даты (по умолчанию текущее время в UTC) для поиска и интервал поиска в днях"""
    date = []
    date.append(str(int(todate.timestamp())))
    date.append(str(int((todate - timedelta(days = interval)).timestamp())))
    return date


def gets_posts_stackoverflow(interval: list, tag_name = "Python", order = "desc", sort = "activity"):
    params = {
            "fromdate": interval[1],
            "todate": interval[0],
            "order": order,
            "sort": sort,
            "tagged": tag_name,
            "site": "stackoverflow"
            }   
  
    url = "https://api.stackexchange.com/2.3/questions"

    response = requests.get(url, params=params)
    return response.json()    
    

if __name__ == '__main__':

    for posts in gets_posts_stackoverflow(input_date())['items']:
        print(posts['title'], end = "\n")
        print(posts["creation_date"], end = "\n")
        print()
