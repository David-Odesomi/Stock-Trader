import yfinance as yf

def  get_current_price(symbol):
    current_price = yf.Ticker(symbol)
    return current_price.fast_info["lastPrice"]