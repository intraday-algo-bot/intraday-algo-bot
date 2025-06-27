# telegram_alert.py - Sends alert message to Telegram
import requests
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_bot_token_here")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "your_chat_id_here")

def send_telegram_alert(symbol, signal, df):
    last_price = df.iloc[-1]['close']
    msg = f"🔔 *{signal} Signal*\n📈 *{symbol}* at ₹{last_price:.2f}\n[Chart](https://www.tradingview.com/symbols/NSE-{symbol})"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
