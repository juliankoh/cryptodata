from pymarketcap import Pymarketcap
coinmarketcap = Pymarketcap()

def price(symbol):
	print (coinmarketcap.ticker(symbol))

price(input())