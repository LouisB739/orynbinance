import requests
import time
from bs4 import BeautifulSoup
import smtplib
import gmail

def binance_monitor():

    url = 'https://www.binance.com/en/support/sections/115000106672'

    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    news2 = soup2.text
        
    while True:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news = soup.text
        time.sleep(15)
        
        if news == news2:
            print("....")
        else:
            gmail.send_mail("v.dalet@gmail.com")
            gmail.send_mail("l2525b@gmail.com")
            response2 = requests.get(url)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            news2 = soup2.text







