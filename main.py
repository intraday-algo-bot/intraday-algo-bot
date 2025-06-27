# Algo Trading Bot using RSI + MACD + EMA with Telegram Alerts and Dhan API + SL/TP
import time
import requests
from dhan import DhanClient
from indicators import calculate_indicators
from telegram_alert import send_telegram_alert
from symbols import stock_list
from dhan_api import place_order

# Dhan Credentials
DHAN_CLIENT_ID = "1000675006"
DHAN_ACCESS_TOKEN = "your_dhan_access_token_here"

dhan = DhanClient(DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN)

# Strategy Configuration
TIMEFRAME = "15m"  # 15-minute candles
RSI_PERIOD = 14
EMA_PERIOD = 50
MAX_TRADES = 3
TRADE_CAPITAL = 10000

# Risk Management
SL_PCT = 0.005  # 0.5%
TARGET_PCT = 0.01  # 1%

def run_strategy():
    trade_count = 0
    for symbol in stock_list:
        try:
            df = dhan.get_ohlc(symbol, interval=TIMEFRAME)
            signal = calculate_indicators(df, rsi_period=RSI_PERIOD, ema_period=EMA_PERIOD)

            if signal in ["BUY", "SELL"]:
                entry_price = df['close'].iloc[-1]

                sl = entry_price * (1 - SL_PCT) if signal == "BUY" else entry_price * (1 + SL_PCT)
                target = entry_price * (1 + TARGET_PCT) if signal == "BUY" else entry_price * (1 - TARGET_PCT)

                send_telegram_alert(symbol, signal, df, sl, target)
                place_order(dhan, symbol, TRADE_CAPITAL, signal, sl, target)

                trade_count += 1

            if trade_count >= MAX_TRADES:
                break
        except Exception as e:
            print(f"Error with {symbol}: {e}")

while True:
    run_strategy()
    time.sleep(900)  # wait for 15 minutes
