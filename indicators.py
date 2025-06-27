# Dummy logic to simulate signals
def calculate_indicators(df, rsi_period=14, ema_period=50):
    # Add real indicator logic later
    return "BUY" if df['close'].iloc[-1] % 2 == 0 else "SELL"
