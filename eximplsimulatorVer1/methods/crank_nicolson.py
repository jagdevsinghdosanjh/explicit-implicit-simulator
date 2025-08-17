from scipy.optimize import root_scalar

def crank_nicolson_step(y, dt):
    def equation(yk1): return yk1 + 0.5 * dt * yk1**2 - (y - 0.5 * dt * y**2)
    sol = root_scalar(equation, bracket=[0, 10], method='bisect')
    return sol.root
