import csv
from termcolor import colored
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
sheetPath = '/home/srivathsan/Documents/Important Documents/crypto_portfolio.csv'

def getPrice(cryptoId):
    return cg.get_price(ids=cryptoId, vs_currencies='inr')

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
# fields.append('Net Profits')
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

# for row in rows:
#     for col, space in zip(row, spaces):
#         print(col + " "*(space-len(col)) + "| ", end='')
#     print

for i in range(len(coins)):
    if profits[i]>0:
        color = colors[1]
    elif profits[i] == 0:
        color = colors[3]
    else:
        color = colors[2]
    print(colored(ticker[i] + " "*(spaces[0]-len(ticker[i])) + ' |' + " "*(spaces[2]-len(str(quantity[i]))) + str(quantity[i]) + ' |' + " "*(spaces[3]-len(str(buyingAverage[i]))) + str(buyingAverage[i]) + ' |' + " "*(spaces[4]-len(str(invested[i]))) + str(invested[i]) + ' |' + " "*(spaces[5]-len(str(current[i]))) + str(current[i]) + ' |' + " "*(spaces[6]-len(str(gains[i]) + '%')) + str(gains[i]) + '%' + ' |', color=color))

print('')

# + " "*(spaces[5]-len(str(current[i]))) + str(current[i]) + ' |' 