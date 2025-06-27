# ✅ main.py - Intraday Algo Bot (RSI + MACD + EMA + Dhan API + Telegram)
import time
from dhan_api import place_order
from indicators import calculate_indicators
from telegram_alert import send_telegram_alert
from symbols import stock_list
from dhan import DhanClient

import os

# Get credentials from environment or hardcode if testing locally
CLIENT_ID = os.getenv("DHAN_CLIENT_ID", "1000675006")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN", "your_token_here")
dhan = DhanClient(CLIENT_ID, ACCESS_TOKEN)

TIMEFRAME = "15m"
MAX_TRADES = 3
TRADE_CAPITAL = 10000

def run_strategy():
    trade_count = 0
    for symbol in stock_list:
        try:
            df = dhan.get_ohlc(symbol, interval=TIMEFRAME)
            signal = calculate_indicators(df)
            if signal in ["BUY", "SELL"]:
                send_telegram_alert(symbol, signal, df)
                place_order(dhan, symbol, TRADE_CAPITAL, signal)
                trade_count += 1
            if trade_count >= MAX_TRADES:
                break
        except Exception as e:
            print(f"Error with {symbol}: {e}")

while True:
    run_strategy()
    time.sleep(900)
