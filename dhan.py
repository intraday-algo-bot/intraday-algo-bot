
class DhanClient:
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

    def get_ohlc(self, symbol, interval):
        import pandas as pd
        from datetime import datetime, timedelta
        import random

        # Generate dummy OHLC data for 20 candles
        end = datetime.now()
        start = end - timedelta(minutes=15*20)
        data = {
            "timestamp": pd.date_range(start, periods=20, freq="15T"),
            "open": [random.uniform(1000, 2000) for _ in range(20)],
            "high": [random.uniform(1000, 2000) for _ in range(20)],
            "low": [random.uniform(1000, 2000) for _ in range(20)],
            "close": [random.uniform(1000, 2000) for _ in range(20)],
        }
        return pd.DataFrame(data)
