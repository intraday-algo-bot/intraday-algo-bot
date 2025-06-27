# Handles placing orders via Dhan API (mock or real)
def place_order(dhan, symbol, capital, signal, sl_price=None, target_price=None):
    try:
        ltp = dhan.get_ltp(symbol)
        quantity = int(capital / ltp)

        order = {
            "symbol": symbol,
            "side": signal,
            "qty": quantity,
            "entry_price": round(ltp, 2),
            "stop_loss": round(sl_price, 2) if sl_price else None,
            "target": round(target_price, 2) if target_price else None
        }

        print(f"✅ Order Placed: {order}")
        return order

    except Exception as e:
        print(f"❌ Order placement failed for {symbol}: {e}")
