# Simple Stock Market
Simple example to calculate metrics for given stocks

## Description
Provide working source code that will :-

- For a given stock,
  - i. Given any price as input, calculate the dividend yield
  - ii. Given any price as input, calculate the P/E Ratio
  - iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price
  - iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

##### Constraints & Notes

1.	No database or GUI is required, all data need only be held in memory.

2.	No prior knowledge of stock markets or trading is required – all formulas are provided below.

##### Global Beverage Corporation Exchange

Stock Symbol  | Type | Last Dividend | Fixed Dividend | Par Value
------------- | ---- | ------------: | :------------: | --------: 
TEA           | Common    | 0  |    | 100
POP           | Common    | 8  |    | 100
ALE           | Common    | 23 |    | 60
GIN           | Preferred | 8  | 2% | 100
JOE           | Common    | 13 |    | 250




## Requirements

- Python 3.6+


## Run

Inside the project directory SuperSimpleStockMarket

```
python main.py
```

## Output window

```
Enter the number of the Option you want:
1. Calculate dividend yield
2. Calculate the P/E Ratio
3. Do a Trade
4. Calculate Volume Weighted Stock Price
5. Calculate the GBCE All Share Index
6. Exit
```

Choose the option according to the need.


## Tests

Inside the project directory SuperSimpleStockMarket

```
python test.py
```

## Author

Vijit Vashishtha


