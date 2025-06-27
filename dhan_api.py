# dhan_api.py - Place simulated order
def place_order(dhan, symbol, capital, signal):
    try:
        price = dhan.get_ltp(symbol)['last_price']
        qty = int(capital / price)
        print(f"Placing {signal} order for {symbol} - Qty: {qty} @ ₹{price}")
        # Replace with real order placement if needed
    except Exception as e:
        print(f"Order failed for {symbol}: {e}")
