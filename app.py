
## 2berius' /CrypTracker0/ ##

from bs4 import BeautifulSoup
import requests


def getMonero():
    response = requests.get('https://www.coingecko.com/en/coins/monero/usd')
    soup = BeautifulSoup(response.text, "html.parser")
    # returns text value of the first instance of class "no-wrap"
    value = soup.select('.no-wrap')
    price = value[0].getText()
    xmr_price = float(price[1:].replace(',', ''))
    return xmr_price


def getBitcoin():
    response = requests.get('https://www.coingecko.com/en/coins/bitcoin/usd')
    soup = BeautifulSoup(response.text, "html.parser")
    value = soup.select('.no-wrap')
    # returns text value of the first instance of class "no-wrap"
    price = value[0].getText()
    btc_price = float(price[1:].replace(',', ''))
    return btc_price


def getEthereum():
    response = requests.get('https://www.coingecko.com/en/coins/ethereum/usd')
    soup = BeautifulSoup(response.text, "html.parser")
    value = soup.select('.no-wrap')
    price = value[0].getText()
    eth_price = float(price[1:].replace(',', ''))
    return eth_price


def cryptoTag():
    crypto = input(
        '1) Monero to USD / BTC / ETH\n'
        '2) Bitcoin to USD / XMR / ETH\n'
        '3) Ethererum to USD / BTC / XMR\n'
        'Enter a number: ')

    if crypto == '1':
        amount = input("Enter Monero amount: ")
        try:
            amount = float(amount)
            xmr2usd = getMonero() * amount
            xmr2btc = xmr2usd / getBitcoin()
            xmr2eth = xmr2usd / getEthereum()
            xmrstring = f'${str(xmr2usd)} in USD\n{str(xmr2btc)} in Bitcoin\n{str(xmr2eth)} in Ethereum\n\n${xmr2usd / amount} is trading price'
            return f'\n\n{xmrstring}\n\n'
        except:
            return '\n\nCalculation failed.\n\n'

    elif crypto == '2':
        amount = input("Enter Bitcoin amount: ")
        try:
            amount = float(amount)
            btc2usd = getBitcoin() * amount
            btc2xmr = btc2usd / getMonero()
            btc2eth = btc2usd / getEthereum()
            btcstring = f'${str(btc2usd)} in USD\n{str(btc2eth)} in Ethereum\n{str(btc2xmr)} in Monero\n\n${btc2usd / amount} is trading price'
            return f'\n\n{btcstring}\n\n'
        except:
            return '\n\nCalculation failed.\n\n'

    elif crypto == '3':
        amount = input("Enter Ethereum amount: ")
        try:
            amount = float(amount)
            eth2usd = getEthereum() * amount
            eth2btc = eth2usd / getBitcoin()
            eth2xmr = eth2usd / getMonero()
            ethstring = f'${str(eth2usd)} in USD\n{str(eth2btc)} in Bitcoin\n{str(eth2xmr)} in Monero\n\n${eth2usd / amount} is trading price'
            return f'\n\n{ethstring}\n\n'
        except:
            return '\n\nCalculation failed.\n\n'

    else:
        return '\n\nInvalid input.\n\n'


if __name__ == "__main__":
    print(cryptoTag())
