import time
import json
import hmac
import hashlib
import requests
from urllib.parse import urljoin, urlencode

API_KEY = 'Ia4YgA3lpF1Y97XdwaJnOov1xUmpqYl0tLiBDMh2zalIXiY3YD1qpUJT5R0KW5gs'
SECRET_KEY = 'DG7lgFt7IOdBboatACSbTqB4ip5cjqeaFpKpAkdSneYep64jYVngx4dJu9FbQSwV'
BASE_URL = 'https://api.binance.com'

headers = {
    'X-MBX-APIKEY': API_KEY
}


class BinanceException(Exception):
    def __init__(self, status_code, data):

        self.status_code = status_code
        if data:
            self.code = data['code']
            self.msg = data['msg']
        else:
            self.code = None
            self.msg = None
        message = f"{status_code} [{self.code}] {self.msg}"

        # Python 2.x
        # super(BinanceException, self).__init__(message)
        super().__init__(message)

def get_time():

    PATH =  '/api/v1/time'
    params = None

    timestamp = int(time.time() * 1000)

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, params=params)
    if r.status_code == 200:
        # print(json.dumps(r.json(), indent=2))
        data = r.json()
        print(f"diff={timestamp - data['serverTime']}ms")
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())



def get_price(symbol):
    PATH = '/api/v3/ticker/price'
    params = {
        'symbol': symbol
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        return (json.dumps(r.json(), indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

def get_order_book(symbol,limit):
    PATH = '/api/v1/depth'
    params = {
        'symbol': symbol,
        'limit': limit
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())


def create_order(symbol,side,quantity,price):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())


def get_all_order(symbol):
    #A faire, sur tous les ordres dispos marche mieux
    PATH = '/api/v3/openOrders'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'recvWindow': 5000,
        'timestamp': timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())







def delete_order(symbol,orderid):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'orderId': orderid,
        'recvWindow': 5000,
        'timestamp': timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = urljoin(BASE_URL, PATH)
    r = requests.delete(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())


