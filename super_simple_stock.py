import datetime
import time

data = {'TEA': {'Type': 'Common', 'Last_Dividend': 0, 'Fixed_Dividend': None, 'Par_Value': 100},
        'POP': {'Type': 'Common', 'Last_Dividend': 8, 'Fixed_Dividend': None, 'Par_Value': 100},
        'ALE': {'Type': 'Common', 'Last_Dividend': 23, 'Fixed_Dividend': None, 'Par_Value': 60},
        'GIN': {'Type': 'Preferred', 'Last_Dividend': 8, 'Fixed_Dividend': 0.02, 'Par_Value': 100},
        'JOE': {'Type': 'Common', 'Last_Dividend': 13, 'Fixed_Dividend': None, 'Par_Value': 250}}
exitProg = 1
tradeList = []

def calculateYield(productType, marketPrice, lastDividend = None, fixedDividend = None, parValue = None):
    dividendYield = 0.0
    if(productType == 'Common'):
        dividendYield = lastDividend / marketPrice
    elif (productType == 'Preferred'):
        dividendYield = (fixedDividend * parValue) / marketPrice
    else:
        dividendYield = None
    return dividendYield

def calculatePERatio(marketPrice, lastDividend):
    return marketPrice / lastDividend

def addTrade (tList):
   
    #timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    timeStamp = datetime.datetime.now()
    quantity = int(input("Please enter the quantity of shares: "))
    sellBuyInd = int(input("Is this a buy or sell (1: BUY/ 2: SELL): "))
    price = float(input("Please enter the price (Example: 4.56): "))
    tList.append({'Time_Stamp': timeStamp, 'Quantity': quantity, 'Sell_Buy': sellBuyInd, 'Price': price})
    return tList

def calculateStockPrice(tList):
    d1 = datetime.datetime.now() + datetime.timedelta(minutes = -15)
    totalQuantityPrice = 0.0
    totalQuantity = 0
    for e in tList:
        if(e['Time_Stamp'] < d1):
            continue
        else:
            print('YAAAS')
            totalQuantity += e['Quantity']
            totalQuantityPrice += e['Quantity'] * e['Price'] 
    return totalQuantityPrice / totalQuantity

def geometric_mean(seq):
    return reduce(lambda x, y: x*y, seq) ** (decimal.Decimal(1)/len(seq))

while(exitProg):
    for e in data:
        print('Product: ' + e)
        print('    ' + str(data[e]))
    print('\n')
    print('OPTIONS')
    print("1. Calculate yield for a product")
    print("2. Calculate P/E ratio for a product")
    print("3. Record a trade")
    print("4. Calculate Volume Weighted Stock Price based on trades in past 15 minutes")
    print("5. GBCE Index")
    choice = int(input('Please select an option (Example: 1): '))

    if(choice == 1):
        pType = input("Please enter the product type: ")
        mPrice = int(input("Please enter the market price: "))
        print('Yield: ')
        print(calculateYield(data[pType]['Type'], mPrice, data[pType]['Last_Dividend'], data[pType]['Fixed_Dividend'], data[pType]['Par_Value']))
    elif(choice == 2):
        pType = input("Please enter the product type: ")
        mPrice = int(input("Please enter the market price: "))
        print('P/E Ratio')
        print(calculatePERatio(mPrice, data[pType]['Last_Dividend']))
    elif(choice == 3):
        addTrade(tradeList)
        print(tradeList)
    elif(choice == 4):
        print(calculateStockPrice(tradeList))
    elif(choice == 5):
        seq =[x['Price'] for x in tradeList]
        print("GBCE All Share Index: ")
        geometric_mean(seq)
    else:
        print('Try again...')
    print('\n\n')
