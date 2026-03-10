class Stock:
    def __init__(self, symbol, buy_price, shares) -> None:
        self.symbol = symbol
        self.buy_price = buy_price
        self.shares = shares

    def current_value(self, current_price):
        return current_price * self.shares

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
