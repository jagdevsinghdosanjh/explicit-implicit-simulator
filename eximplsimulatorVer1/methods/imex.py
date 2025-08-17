def imex_step(y, dt):
    # Explicit part: nonlinear term
    y_explicit = y - dt * y**2
    # Implicit part: linear damping
    return y_explicit / (1 + dt)
