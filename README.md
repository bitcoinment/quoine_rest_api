![quoine_rest_api](https://raw.github.com/bitcoinment/quoine_rest_api/master/quoine_rest_api.gif)

# Python client for the Quoine API

Getting fresh orders in real time. 
The unofficial Python client for the Quoine API.

[Check out the Interactive Demo](http://kupi.net/p/docs-api)

With this module, you can develop your own crypto-bots, analyze crypto-markets and of course, make money.

Our web-service works 24 hours and keeps high loads

The data of all exchanges come in a single format and contain extended information (links for switching to trading pairs, best asks and bids, exchange rates and much more).

---

- FREE!
- The actuality of orders is 5-30 seconds!
- Data from most exchanges
- Round-the-clock support


### Installation Instructions
    $ pip3 install quoine-rest-api==1.4.4

### Init example
```python
from quoine_rest_api import quoine_rest_api
```

### Stocks API
```python
# Get all stocks
quoine_rest_api.KUPINET('freeApi').Stocks().getList()

# Get orders by Stock name
quoine_rest_api.KUPINET('freeApi').Stocks('Qryptos').getOrders('ETH','BTC')

# Get all pairs from the Stock
quoine_rest_api.KUPINET('freeApi').Stocks('Qryptos').getAllPairs()
```
### Pairs API
```python
# Find best prices for Pair in all Stocks
quoine_rest_api.KUPINET('freeApi').Pair('LTC','ETH').getBestPrices()
```
### Find Best Prices API
```python
# Find best ASK
quoine_rest_api.KUPINET('freeApi').BestPrices('LTC').Ask()

# Find best BID
quoine_rest_api.KUPINET('freeApi').BestPrices('LTC').Bid()
```
### Cryptocurrency Converter (Calculator) API
```python
# Coins list
quoine_rest_api.KUPINET('freeApi').Calc().Data()

# Convert Coin to Coin
quoine_rest_api.KUPINET('freeApi').Calc('LTC','ETH').Amount(10)
```

## In the future
- Unloading historical trade data
- Multi-trading through a single terminal
- Tool for crypto arbitrage
- API for JavaScript, PHP, C#
- Launch of a decentralized exchange
- Widget (calculator) for integration with sites


## About us
 We are a team of crypto developers. Our goal is to make the most convenient crypto services possible.
[Contact with us](http://kupi.net/p/support)