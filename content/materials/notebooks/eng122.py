import numpy as np
from scipy.integrate import ode


def _rk4(t, dt, x, f, args=None):
    """4th-order Runge-Kutta integration step."""
    x = np.asarray(x)
    k1 = np.asarray(f(x, t, *args))
    k2 = np.asarray(f(x + 0.5*dt*k1, t + 0.5*dt, *args))
    k3 = np.asarray(f(x + 0.5*dt*k2, t + 0.5*dt, *args))
    k4 = np.asarray(f(x + dt*k3, t + dt, *args))
    return x + dt*(k1 + 2*k2 + 2*k3 + k4)/6.0


def rk4int(func, x0, t, args=None):
    """4th-order Runge-Kutta integration.

    Parameters
    ----------
    func : callable(x, t, *args)
        Function that returns the derivatives of the state variables at time t.
    x0 : array_like, shape(n,)
        Initial values of the state variables.
    t : array, shape(m,)
        Array of time values at which to solve.
    args : tuple, optional
        Additional arguments to `func`.

    Returns
    -------
    x : ndarray, shape(m, n)
        Array containing the values of the state variables at the
        specified time values in `t`.

    """
    x = np.zeros((len(t), len(x0)))
    x[0, :] = x0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        x[i] = _rk4(t[i], dt, x[i-1], func, args)
    return x


def odeint(f, x0, t, args=tuple(), integrator='vode', method=None):

    def f_switched(t, x, *args):
        return f(x, t, *args)

    routine = ode(f_switched)
    routine.set_integrator(integrator, method='adams')
    routine.set_initial_value(x0, t[0])
    routine.set_f_params(*args)

    results = np.zeros((len(t), len(x0)))

    for i, ti in enumerate(t):
        if routine.successful():
            routine.t = ti
            results[i] = routine.integrate(ti + t[i + 1])

    return results