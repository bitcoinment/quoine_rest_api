# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import time
import requests
import json

# GLOBAL_DOMAIN = 'http://127.0.0.1:8000'
GLOBAL_DOMAIN = 'http://kupi.net'


def jprint(arr):
    print(json.dumps(arr, indent=4, sort_keys=False))

def apiRoute(arr):

    if not 'KUPINET_API_KEY' in globals():
        return {
            'error': True,
            'message': 'Variable KUPINET_API_KEY not specified!'
        }


    conf_site = GLOBAL_DOMAIN+'/api/v1/'+KUPINET_API_KEY+'/'
    postfix = '/'.join(arr) + '/'
    url = conf_site + postfix.lower()

    try:
        print(url)
        r = requests.get(url)
        response = r.content.decode('utf8')
        if len(response) > 0:
            data = json.loads(response)
            return data
        else:
            print('Server error')
            return False


    except Exception as e:
        print('Error >> '+str(e))
        return False



class NET:

    def __init__(self):
        pass



    class Stocks:

        def __init__(self, stock_name=False):
            self.stock_name = stock_name.strip() if stock_name else False

        def getOrders(self, coin_from, coin_to):
            coin_from_ = coin_from.strip().lower()
            coin_to_   = coin_to.strip().lower()


            return apiRoute(['stocks',self.stock_name,'orders',coin_from_,coin_to_])

        def getList(self):
            return apiRoute(['stocks-list'])

        def getAllPairs(self):
            return apiRoute(['stocks', self.stock_name, 'all-pairs'])


    class Pair:
        def __init__(self, coin_from=False, coin_to=False):
            self.coin_from_ = coin_from.strip().lower()
            self.coin_to_ = coin_to.strip().lower()

        def getBestPrices(self):

            return apiRoute(['pairs', 'best-prices', self.coin_from_, self.coin_to_])


    class BestPrices:
        def __init__(self, coin):
            self.coin_ = coin.strip().lower()

        def Ask(self):
            return apiRoute(['best-prices', 'ask', self.coin_])

        def Bid(self):
            return apiRoute(['best-prices', 'bid', self.coin_])



    class Calc:
        def __init__(self, coin_from=False, coin_to=False):
            self.coin_from = False
            self.coin_to = False

            if coin_from and coin_to:
                self.coin_from = coin_from.strip().lower()
                self.coin_to = coin_to.strip().lower()

        def Amount(self, amount):
            self.amount = str(float(amount))

            if not self.coin_from or not self.coin_to:
                return {
                    'error': True,
                    'message': 'Coins not defined',
                }

            return apiRoute(['calc', 'math', self.coin_from, self.coin_to, self.amount])


        def Data(self):
            return apiRoute(['calc', 'data'])



if __name__ == "__main__":
    pass

    KUPINET_API_KEY = 'freeApi'

    # orders = NET.Stocks('Binance').getOrders('ETH','BTC')
    # jprint(orders)
    #
    # allStocks = NET.Stocks().getList()
    # jprint(allStocks)

    #
    # pairs = NET.Stocks('Binance').getAllPairs()
    # jprint(pairs)

    # prices = NET.Pair('LTC','ETH').getBestPrices()
    # jprint(prices)


    # bestAsk = NET.BestPrices('LTC').Ask()
    # bestBid = NET.BestPrices('LTC').Bid()
    # jprint(bestAsk)
    # jprint(bestBid)


    # calcMath = NET.Calc('LTC','ETH').Amount(10)
    # jprint(calcMath)

    # calcData = NET.Calc().Data()
    # jprint(calcData)



# https://stackedit.io/app#
# pip3 install KUPINET
# from KUPINET import KUPI
#
# orders = KUPI.NET.Stocks('Binance').getOrders('ETH','BTC')
# print(orders)
#
# pairs = KUPI.NET.Stocks('Binance').getAllPairs()
# print(pairs)
#
# prices = KUPI.NET.Pair('LTC', 'ETH').getBestPrices()
# print(prices)
