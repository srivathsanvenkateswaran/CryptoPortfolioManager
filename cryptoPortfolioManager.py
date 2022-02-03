import csv
from termcolor import colored
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
sheetPath = '/home/srivathsan/Documents/Important Documents/crypto_portfolio.csv'
fiatCurrency = 'inr'

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

colors = ['yellow', 'green', 'red', 'white']
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

current = [round(quantity[i]*getPrice(coins[i])[coins[i]]['inr'], 2) for i in range(len(coins))]
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
    netProfit *= 0.7

print(colored(' '*20 + f'Net Profits: {netProfit}', clr))
print(colored(' '*20 + f'Net Portfolio {upOrDown} by ', colors[0]), end="")
print(colored(f'{round(netProfit/totalInvested * 100, 2)} %', clr))
print()