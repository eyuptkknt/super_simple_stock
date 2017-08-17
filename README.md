# super_simple_stock


Requirements
1. Provide working source code that will :

a. For a given stock,
i. Given a market price as input, calculate the dividend yield
ii. Given a market price as input, calculate the P/E Ratio
iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and
trade price
iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes
b. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

# formulas is uploaded as formulas.png
you can find and useformulas in formulas.png file to do.



# small set of data as dictionary

data = {'TEA': {'Type': 'Common', 'Last_Dividend': 0, 'Fixed_Dividend': None, 'Par_Value': 100},
        'POP': {'Type': 'Common', 'Last_Dividend': 8, 'Fixed_Dividend': None, 'Par_Value': 100},
        'ALE': {'Type': 'Common', 'Last_Dividend': 23, 'Fixed_Dividend': None, 'Par_Value': 60},
        'GIN': {'Type': 'Preferred', 'Last_Dividend': 8, 'Fixed_Dividend': 0.02, 'Par_Value': 100},
        'JOE': {'Type': 'Common', 'Last_Dividend': 13, 'Fixed_Dividend': None, 'Par_Value': 250}}
       
  
