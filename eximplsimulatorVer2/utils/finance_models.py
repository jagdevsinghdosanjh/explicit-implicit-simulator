import pandas as pd

def forward_euler_forecast(df, days):
    prices = df['Close'].values
    forecast = [prices[-1]]
    dt = 1  # daily step

    for _ in range(days):
        change = (prices[-1] - prices[-2])  # simple derivative
        next_price = forecast[-1] + dt * change
        forecast.append(next_price)

    return pd.DataFrame({'Forecast': forecast})
