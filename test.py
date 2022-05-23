import random
import unittest
import json
import os
from stock_market import StockMarket


class StockMarketTest(unittest.TestCase):
    symbols = [1, 2, 3, 4, 5]
    types = [1, 2]
    quantities = range(0, 1000, 5)
    prices = [10, 10000, 73, 29.6, 1, 923, 0]

    @classmethod
    def setUpClass(cls):
        cls.stock_mapping = {1: "TEA", 2: "POP", 3: "ALE", 4: "GIN", 5: "JOE", 6: "TEST"}
        cls.indicator_mapping = {1: "BUY", 2: "SELL"}
        cls.symbol = 6
        cls.quantity = 22
        cls.indicator = 1
        cls.traded_price = 90
        cls.price = 100

    def test_record_trade(self):
        StockMarket().record_trade(self.symbol, self.quantity,
                                   self.indicator, self.traded_price)
        if not os.path.isfile('trade_record.json'):
            assert False
        with open('trade_record.json', 'r') as trade_record_file_obj:
            trade_data = json.load(trade_record_file_obj)
        stock = next((item for item in trade_data if item["stock_symbol"] == self.stock_mapping[self.symbol]), None)
        print(stock)
        if stock and len(stock) > 0:
            assert True

    def test_stock_price(self):
        vol_weighted_price = StockMarket().volume_weighted_stock_price(self.stock_mapping[self.symbol])
        message = "First value and second value are not equal !"
        self.assertEqual(vol_weighted_price, self.traded_price, message)

    def test_dividend_yield(self):
        dividend_yield = StockMarket().calculate_dividend_yield(self.symbol, self.price)
        message = "First value and second value are not equal !"
        self.assertEqual(dividend_yield, 0, message)

    def test_p_e_ratio(self):
        pe_ratio = StockMarket().calculate_pe_ratio(self.symbol, self.price)
        message = "First value and second value are not equal !"
        self.assertEqual(pe_ratio, 0, message)

    def test_gbce(self):
        all_share_index = StockMarket().all_share_index()
        if all_share_index:
            assert True


if __name__ == "__main__":
    def suite():
        """
            Gather all the tests from this module in a test suite and run in specific order.
        """
        suite = unittest.TestSuite()
        suite.addTest(StockMarketTest('test_record_trade'))
        suite.addTest(StockMarketTest('test_stock_price'))
        suite.addTest(StockMarketTest('test_dividend_yield'))
        suite.addTest(StockMarketTest('test_dividend_yield'))
        suite.addTest(StockMarketTest('test_gbce'))
        return suite

    custom_suit = suite()
    runner = unittest.TextTestRunner()
    runner.run(custom_suit)
