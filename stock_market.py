import csv
import json
import os
from datetime import datetime, timedelta


class StockMarket:
    def __init__(self):
        self.stock_mapping = {1: "TEA", 2: "POP", 3: "ALE", 4: "GIN", 5: "JOE", 6: "TEST"}
        self.indicator_mapping = {1: "BUY", 2: "SELL"}
        self.sample_data = list(csv.DictReader(open('gbce_sample_data.csv')))
        self.trade_record_file = 'trade_record.json'
        if not os.path.isfile(self.trade_record_file):
            with open(self.trade_record_file, 'w'):
                pass
        if os.stat(self.trade_record_file).st_size == 0:
            self.trade_data = []
        else:
            with open(self.trade_record_file, 'r') as trade_record_file_obj:
                self.trade_data = json.load(trade_record_file_obj)

    def calculate_dividend_yield(self, symbol, price):
        """ Calculates the dividend yield for given stock. """
        try:
            stock_symbol = self.stock_mapping[symbol]
        except KeyError:
            return "Enter Valid Stock Symbol"
        try:
            if float(price) == 0.0:
                return "Enter valid price"
        except ValueError:
            return "Enter valid price"

        stock = next((item for item in self.sample_data if item["stock_symbol"] == stock_symbol), None)
        dividend_yield = 0
        price = float(price)
        if stock['stock_type'] == "Common":
            try:
                last_dividend = float(stock.get('last_dividend', 0))
                dividend_yield = last_dividend / price
            except ZeroDivisionError:
                return dividend_yield
        elif stock['stock_type'] == "Preferred":
            try:
                fixed_dividend = float(stock.get('fixed_dividend', 0)) / 100
                par_value = float(stock.get('par_value', 0))
                dividend_yield = fixed_dividend * par_value / price
            except ZeroDivisionError:
                return dividend_yield
        else:
            return False
        return dividend_yield

    def calculate_pe_ratio(self, symbol, price):
        """ Calculate P/E Ratio for given stock. """

        dividend_yield = self.calculate_dividend_yield(symbol, price)
        if not dividend_yield:
            return dividend_yield
        else:
            try:
                pe_ratio = float(price) / float(dividend_yield)

            except ZeroDivisionError:
                pe_ratio = 0
            return pe_ratio

    def record_trade(self, symbol, quantity, indicator, traded_price):
        """ Record a new trade in the stock. """

        try:
            stock_symbol = self.stock_mapping[symbol]
        except KeyError:
            return "Enter Valid Stock Symbol"
        try:
            indicator = self.indicator_mapping[indicator]
        except KeyError:
            return "Enter Valid Indicator"
        quantity = int(quantity)
        traded_price = float(traded_price)

        try:
            self.create_trade_record_data(stock_symbol, quantity,
                                          indicator, traded_price, str(datetime.now()))
            json_object = json.dumps(self.trade_data, indent=4)
            with open(self.trade_record_file, "w") as outfile:
                outfile.write(json_object)
            print("Trade_record ", json_object)
        except Exception:
            print("Trade data Not Added")

    def volume_weighted_stock_price(self, stock_symbol):
        """ Calculate stock price for given stock based on trades from last 15 min. """

        trade_time = datetime.now() - timedelta(minutes=15)
        stock_quantity_sum = 0
        sum_stock_trade_price = 0

        if len(self.trade_data) > 0:
            for record in self.trade_data:
                record_trade_timestamp = datetime.fromisoformat(record['trade_timestamp'])
                if record['stock_symbol'] == stock_symbol and record_trade_timestamp >= trade_time:
                    print(record)
                    stock_quantity_sum += record['quantity']
                    sum_stock_trade_price += (record['quantity'] * record['traded_price'])
            if sum_stock_trade_price and stock_quantity_sum:
                vol_weight_stock_price = float(sum_stock_trade_price / stock_quantity_sum)
                print("Volume Weighted Stock Price :  ", vol_weight_stock_price)
                return vol_weight_stock_price
            else:
                return "Trade record is empty for the stock {0} in the past 15 minutes".format(stock_symbol)
        else:
            print("Trade Record is empty")

    def all_share_index(self):
        """ Calculate the GBCE All Share Index using the geometric mean of prices for all stocks. """

        trade_time = datetime.now() - timedelta(minutes=15)
        stock_quantity_sum = 0
        sum_stock_trade_price = 0

        if len(self.trade_data) > 0:
            for record in self.trade_data:
                record_trade_timestamp = datetime.fromisoformat(record['trade_timestamp'])
                if record_trade_timestamp >= trade_time:
                    stock_quantity_sum += record['quantity']
                    sum_stock_trade_price += (record['quantity'] * record['traded_price'])
            if sum_stock_trade_price and stock_quantity_sum:
                # stock_quantity_sum root sum_stock_trade_price
                all_share_index = sum_stock_trade_price ** (1 / stock_quantity_sum)
                print("ALL Share Index :  ", float(all_share_index))
                return float(all_share_index)
            else:
                print("No Trade in last 15 mins")
                return False
        else:
            print("Trade Record is empty")
            return False

    def create_trade_record_data(self, stock_symbol, quantity, indicator, traded_price, current_timestamp):
        record = {
            "stock_symbol": stock_symbol,
            "quantity": quantity,
            "indicator": indicator,
            "traded_price": traded_price,
            "trade_timestamp": current_timestamp
        }
        self.trade_data.append(record)
