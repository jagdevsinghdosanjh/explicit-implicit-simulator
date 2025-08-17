import numpy as np
import pandas as pd

def euler_forecast(S0, r, T, dt):
    """
    Euler method for simple interest-based forecasting.
    S0: Initial value
    r: Interest rate
    T: Total time (in years)
    dt: Time step
    """
    N = int(T / dt)
    times = np.linspace(0, T, N)
    values = [S0]

    for _ in range(1, N):
        S_prev = values[-1]
        S_new = S_prev + r * S_prev * dt
        values.append(S_new)

    return pd.DataFrame({'Time': times, 'Forecast': values})


def crank_nicolson_forecast(S0, r, T, dt):
    """
    Crank-Nicolson method for more stable forecasting.
    Assumes linear growth with midpoint averaging.
    """
    N = int(T / dt)
    times = np.linspace(0, T, N)
    values = [S0]

    for _ in range(1, N):
        S_prev = values[-1]
        S_mid = S_prev + 0.5 * r * S_prev * dt
        S_new = S_prev + r * S_mid * dt
        values.append(S_new)

    return pd.DataFrame({'Time': times, 'Forecast': values})
