PORTFOLIO_FILE = "data/portfolio.json"
from .api import get_current_price
from .storage import save_portfolio, load_portfolio
from .models import Stock, Portfolio
import argparse

def main():
    parser = argparse.ArgumentParser(description="Stock Portfolio Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="add a stock")
    add_parser.add_argument("symbol", type=str)
    add_parser.add_argument("buy_price", type=float)
    add_parser.add_argument("shares", type=float)

    remove_parser = subparsers.add_parser("remove", help="remove a stock")
    remove_parser.add_argument("symbol")

    view_parser = subparsers.add_parser("view", help="List all stocks in the portfolio")

    args = parser.parse_args()

    if args.command == "add":
         portfolio = load_portfolio(PORTFOLIO_FILE)
         stock = Stock(args.symbol, args.buy_price, args.shares)
         portfolio.add_stock(stock)
         print(f"Added {args.symbol} to portfolio!")
         save_portfolio(portfolio, "data/portfolio.json")
    elif args.command == "remove":
         portfolio = load_portfolio("data/portfolio.json")
         portfolio.remove_stock(args.symbol)
         save_portfolio(portfolio, "data/portfolio.json")
         print(f"Removed {args.symbol} from the portfolio!")
    elif args.command == "view":
         portfolio = load_portfolio("data/portfolio.json")
         print(portfolio.stocks)

if __name__ == "__main__":
    main()