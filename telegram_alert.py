import requests

TELEGRAM_TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_chat_id"

def send_telegram_alert(symbol, signal, df, sl=None, target=None):
    entry = df['close'].iloc[-1]
    message = f"""
🔔 *{signal} Signal*
📈 *{symbol}* at ₹{entry:.2f}
🎯 Target: ₹{target:.2f}
🛑 Stop Loss: ₹{sl:.2f}
🔗 [Chart](https://www.tradingview.com/symbols/NSE-{symbol})
"""
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        )
        print(f"📩 Telegram alert sent for {symbol}.")
    except Exception as e:
        print(f"❌ Telegram alert failed: {e}")
