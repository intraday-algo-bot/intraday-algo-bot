# indicators.py - Calculates RSI, MACD, EMA
import pandas as pd
import ta

def calculate_indicators(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    df['EMA'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    df['MACD'] = ta.trend.MACD(df['close']).macd_diff()
    latest = df.iloc[-1]

    if latest['RSI'] < 30 and latest['MACD'] > 0 and latest['close'] > latest['EMA']:
        return "BUY"
    elif latest['RSI'] > 70 and latest['MACD'] < 0 and latest['close'] < latest['EMA']:
        return "SELL"
    else:
        return "HOLD"
