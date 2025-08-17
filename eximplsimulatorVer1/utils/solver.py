def simulate(method_func, y0, dt, steps):
    y_values = [y0]
    for _ in range(steps):
        y_next = method_func(y_values[-1], dt)
        y_values.append(y_next)
    return y_values
