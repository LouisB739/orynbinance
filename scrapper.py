import requests
import time
from bs4 import BeautifulSoup
import smtplib
import gmail
import whatsapp


def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)


def binance_monitor():

    url = 'https://www.binance.com/en/support/categories/115000056351'

    response2 = requests.get(url)
    news_title_array = []
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    for titles in soup2.find_all(class_="article-list-link"):
        news_title_array.append(titles.get_text())
    
    while True:
        response = requests.get(url)
        news_title_array2 = []
        soup = BeautifulSoup(response.text, 'html.parser')

        for titles in soup.find_all(class_="article-list-link"):
            news_title_array2.append(titles.get_text())


        time.sleep(15)
        
    
        if news_title_array2 == news_title_array:
            print("....")
        else:
                message = diff(news_title_array2,news_title_array)
                gmail.send_mail("l2525b@gmail.com")
                whatsapp.send_text(str(message))
                response2 = requests.get(url)
                news_title_array = []
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                for titles in soup2.find_all(class_="article-list-link"):
                    news_title_array.append(titles.get_text())

