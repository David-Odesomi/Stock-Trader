import json
from .models import Stock, Portfolio

def save_portfolio(portfolio, filepath):
    data = [{"symbol": stock.symbol, "buy_price": stock.buy_price, "shares": stock.shares} for stock in portfolio.stocks]

    with open(filepath,"w") as f:
        json.dump(data, f)

def load_portfolio(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    portfolio = Portfolio()
    for item in data:
        stock = Stock(item["symbol"], item["buy_price"], item["shares"])
        portfolio.add_stock(stock)
    return portfolio
