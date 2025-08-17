import numpy as np
import pandas as pd

def gbm_forecast(S0, mu, sigma, days, n_paths=100):
    dt = 1  # daily step
    forecasts = np.zeros((days + 1, n_paths))
    forecasts[0] = S0

    for t in range(1, days + 1):
        Z = np.random.standard_normal(n_paths)
        forecasts[t] = forecasts[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return pd.DataFrame(forecasts)
