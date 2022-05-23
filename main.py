from stock_market import StockMarket

if __name__ == '__main__':
    menu_main = "Enter the number of the Option you want:\n" \
                "1. Calculate dividend yield\n" \
                "2. Calculate the P/E Ratio\n" \
                "3. Do a Trade\n" \
                "4. Calculate Volume Weighted Stock Price\n" \
                "5. Calculate the GBCE All Share Index\n" \
                "6. Exit\n"

    menu_stocks = "Choose a stock:\n" \
                  "1. TEA\n" \
                  "2. POP\n" \
                  "3. ALE\n" \
                  "4. GIN\n" \
                  "5. JOE\n"

    menu_buy_sell = "Please select:\n" \
                    "1. BUY\n" \
                    "2. SELL\n"

    menu_option_list = list(range(1, 7))
    while True:
        option = int(input(menu_main))
        if option not in menu_option_list:
            print("Invalid Option, Select from below options only: \n")

        elif option == 6:
            break

        elif option == 1:
            symbol = int(input(menu_stocks))
            price = input("Enter the stock price:\n")
            dividend_yield = StockMarket().calculate_dividend_yield(symbol, price)
            print("Dividend Yield : %s\n" % dividend_yield)

        elif option == 2:
            symbol = int(input(menu_stocks))
            price = input("Enter the stock price: \n")

            pe_ratio = StockMarket().calculate_pe_ratio(symbol, price)
            print("P/E Ratio : %s\n" % pe_ratio)

        elif option == 3:
            symbol = int(input(menu_stocks))
            quantity = input("Quantity of shares: \n")
            indicator = int(input(menu_buy_sell))
            traded_price = input("Enter Trade Price: \n")
            StockMarket().record_trade(symbol, quantity, indicator, traded_price)

        elif option == 4:
            symbol = int(input(menu_stocks))
            StockMarket().volume_weighted_stock_price(symbol)

        elif option == 5:
            StockMarket().all_share_index()
