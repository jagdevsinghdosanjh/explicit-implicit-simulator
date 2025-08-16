def forward_euler_step(y, dt):
    return y - dt * y**2
