import requests
import time
from bs4 import BeautifulSoup
import smtplib
import gmail
import whatsapp

def binance_monitor():

    url = 'https://www.binance.com/en/support/sections/115000202591'

    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    news2 = soup2.find("li", class_="article-list-item")
        
    while True:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news = soup.find("li", class_="article-list-item")

        time.sleep(15)
        
        if news == news2:
            print("....")
        else:
            message = news.text
            gmail.send_mail("v.dalet@gmail.com","l2525b@gmail.com")
            whatsapp.send_text(message)
            response2 = requests.get(url)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            news2 = soup2.find("li", class_="article-list-item")










