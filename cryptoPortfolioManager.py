import csv
from termcolor import colored
from pycoingecko import CoinGeckoAPI
import sys

# Handling system args
if(len(sys.argv) > 1):
    if(sys.argv[1] in ['-h', '--help']):
        print(
            '''Usage: python3 cryptoPortfolioManager.py [OPTION]...        
Crypto Portfolio Manager - A CLI Tool to keep track of your crypto Portfolio.

List of supported long options and short options.
  -h,  --help         Display the Help command.
  -w, --weightage     Show the crypto Portfolio along with Coin Weightage.
            '''
        )
        sys.exit()

cg = CoinGeckoAPI()
sheetPath = '/home/srivathsan/Documents/Important Documents/crypto_portfolio.csv'
fiatCurrency = 'inr'

def getUSTaxBacket(totalProfits):
    if totalProfits <= 40400:
        return 1
    elif totalProfits >= 40401 and totalProfits <= 445850:
        return 0.85
    elif totalProfits >= 445851:
        return 0.8

def getTaxMultiplier(totalProfits):
    if fiatCurrency == 'inr':
        taxMultiplier = 0.4
    elif fiatCurrency == 'usd':
        taxMultiplier = getUSTaxBacket(totalProfits=totalProfits)

def getPrice(cryptoId):
    return cg.get_price(ids=cryptoId, vs_currencies=fiatCurrency)

fields = []
rows = []
with open(sheetPath, 'r') as file:
    csvreader = csv.reader(file)
    fields = next(csvreader)
    fields[0] = 'Coin'
    for row in csvreader:
        rows.append(row)

colors = ['yellow', 'green', 'red', 'white', 'cyan']
spaces = []
fields.append('Invested')
fields.append('Current Value')
fields.append('Gains (%)')
for field in fields:
    if len(field) < 5:
        spaces.append(5)
    elif len(field) < 10:
        spaces.append(10)
    else:
        spaces.append(15)

for field in fields:
    if field == 'Coingecko ID':
        continue
    print(colored(" "*(spaces[fields.index(field)]-len(field)) + field + " |", colors[0]), end='')

print('\n')

ticker = []
coins = []
quantity = []
buyingAverage = []

for row in rows:
    ticker.append(row[0])
    coins.append(row[1])
    quantity.append(float(row[2]))
    buyingAverage.append(float(row[3]))

current = [round(quantity[i]*getPrice(coins[i])[coins[i]][fiatCurrency], 2) for i in range(len(coins))]
invested = [round(quantity[i]*buyingAverage[i], 2) for i in range(len(coins))]
profits = [current[i]-invested[i] for i in range(len(coins))]
gains = [round(profits[i]/invested[i] * 100, 2) for i in range(len(coins))]

for i in range(len(coins)):
    if profits[i]>0:
        color = colors[1]
    elif profits[i] == 0:
        color = colors[3]
    else:
        color = colors[2]
    print(colored(ticker[i] + " "*(spaces[0]-len(ticker[i])) + ' |' + " "*(spaces[2]-len(str(quantity[i]))) + str(quantity[i]) + ' |' + " "*(spaces[3]-len(str(buyingAverage[i]))) + str(buyingAverage[i]) + ' |' + " "*(spaces[4]-len(str(invested[i]))) + str(invested[i]) + ' |' + " "*(spaces[5]-len(str(current[i]))) + str(current[i]) + ' |' + " "*(spaces[6]-len(str(gains[i]) + '%')) + str(gains[i]) + '%' + ' |', color=color))

print('')

totalInvested = round(sum(invested), 2)
totalCurrent = round(sum(current), 2)
totalProfits = round(totalCurrent - totalInvested, 2)

print(colored(' '*20 + f'Total Invested: {totalInvested}', colors[0]))
print(colored(' '*20 + f'Total Current: {totalCurrent}', colors[0]))
if totalProfits > 0:
    clr = colors[1]
    upOrDown = 'up'
else:
    clr = colors[2]
    upOrDown = 'down'

print(colored(' '*20 + f'Total Profits: {totalProfits}', clr))
print(colored(' '*20 + f'Portfolio {upOrDown} by ', colors[0]), end="")
print(colored(f'{round(totalProfits/totalInvested * 100, 2)} %', clr))
print()

netProfit = totalProfits
if upOrDown == 'up':
    netProfit *= getTaxMultiplier(totalProfits=totalProfits)

print(colored(' '*20 + f'Net Profits: {netProfit}', clr))
print(colored(' '*20 + f'Net Portfolio {upOrDown} by ', colors[0]), end="")
print(colored(f'{round(netProfit/totalInvested * 100, 2)} %', clr))
print()

if(len(sys.argv) > 1):
    if(sys.argv[1] in ['-w', '--weightage']):
        investedDict = {}

        for i in range(0, len(ticker)):
            investedDict[ticker[i]] = invested[i]

        investedDict = dict(sorted(investedDict.items(), key=lambda item: item[1]))
        investedDict = dict(reversed(list(investedDict.items())))

        print(colored(' '*10 + 'Portfolio Weightage: ', colors[1]))
        print()

        print(' '*10 + 'Coin  |  Invested |  Share ')

        for key, value in investedDict.items():
            coinShare = str(round(value/totalInvested * 100, 2))
            print(colored(' '*10 + key + ' '*(6-len(key)), colors[0]) + '|' + colored(' '*(10-len(str(value))) + str(value), colors[0]), end = " ")
            print('|' + colored(' '*(7-len(coinShare)) + coinShare + ' %', colors[4]))
