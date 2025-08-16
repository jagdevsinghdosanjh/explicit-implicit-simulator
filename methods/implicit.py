from scipy.optimize import root_scalar

def backward_euler_step(y, dt):
    def equation(yk1): return (yk1 - y)/dt + yk1**2
    sol = root_scalar(equation, bracket=[0, 10], method='bisect')
    return sol.root
