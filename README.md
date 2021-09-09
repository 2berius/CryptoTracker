# CryptoTracker
A Python script that scans coingecko.com for Bitcoin, Ethereum, and Monero prices, and allows the user to input amount values through their terminal/command line.


## How to Use
It's suggested that you run this program through your terminal/command line. Then, follow the steps:

1. Once you start running the script, you'll be prompted to enter your choice. Enter 1 for Monero, 2 for Bitcoin, or 3 for Ethereum.

2. You'll now be asked to enter the amount of cryptocurrency that you want to check. For instance, if you want to see how much 0.568 Bitcoin is worth, you'd enter "0.568" (minus quotes) into the prompt.

3. The program will output the following info: How much the amount you entered is worth in USD at the exact time you ran the script, how much it is worth in the other two cryptocurrencies listed, and the current trading price (price of one (1) crypto coin).


## Example of "How to Use"
Say you have 0.134 Bitcoin in your wallet, and you want to see how much it is worth in dollars, how it translates to other cryptocurrencies, and what the current trading price is. In order to do this, you would run main.py and enter "2" into the first prompt to select Bitcoin as your choice. Then, you would enter "0.134" into the next prompt to lock in the amount of Bitcoin that you want to see the price for. Finally, the program will use the current prices from coingecko.com to tell you how much the amount of Bitcoin you entered is worth at that exact moment, how much Monero and Ethereum you could get for it, and what the current trading price is. All data used comes directly from coingecko.com and is accurate to the exact time you ran the program (maybe delayed by 1-2 seconds but accurate nonetheless).


## Future Updates
Mainly adding this for myself, but feel free to see what updates are in store.

- Cap results to 4-6 decimal places, maximum (.format()).
- Re-organize the final output (order is ugly).
- ADD BETTER COMMENTS (I know, my comments are virtually non-existent and bad).
- Change to Yahoo Finance (perhaps?)
