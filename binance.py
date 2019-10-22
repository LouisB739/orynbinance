import requests


def get_price_ticker(symbol):
    params = {"symbol" : symbol}
    response = requests.get(" https://api.binance.com//api/v3/ticker/price",params).json()
    print(response['price'])
    return response['price'] 

def get_price_changes(symbol):
    params = {"symbol" : symbol}
    response = requests.get(" https://api.binance.com/api/v3/ticker/24hr", params)
    print(response.json())
    return response 


def get_order_book_ticker(symbol):
    params = {"symbol" : symbol}
    response = requests.get(" https://api.binance.com/api/v3/ticker/bookTicker", params).json()
    return response 

def get_askprice_askqty(symbol):
   order_book_ticker = get_order_book_ticker(symbol)
   askprice = order_book_ticker['askPrice']
   askQty = order_book_ticker['askQty']
   print(askprice,askQty)

def get_max_price(symbol,percent_range):
    order_book_ticker = get_order_book_ticker(symbol)
    askprice = float(order_book_ticker['askPrice'])
    toprange = askprice * percent_range
    print(toprange)
    return toprange

def get_exchange_time():
    servertime = requests.get(" https://api.binance.com///api/v3/time").json()
    return str(servertime['serverTime'])


def create_limit_order(symbol,quantity,price):

    params = { "symbol" : symbol ,
            "types" : "limit",
            "timeInForce"	: "GTC",
            "quantity" :quantity,
                "price"	: price,
                "timestamp"	: get_exchange_time()
    }
    return params

    


def place_order(limit_order):
   params = {"symbol" : limit_order['symbol'] ,
   "side":"buy",
    "types" : "limit",
    "timeInForce"	: "GTC",
    "quantity" :limit_order["quantity"],
    "price"	: limit_order["price"],
    "timestamp"	: get_exchange_time()
   }
   print(params)
   server = requests.post("https://api.binance.com///api/v3/order/test",params).json()   
   print(server) 


def get_current_order():
    server = requests.get("https://api.binance.com///api/v3/openOrders").json()
    print(server)


    


place_order(create_limit_order("BTCUSDT",1,get_max_price("BTCUSDT",1.15)))


get_current_order






