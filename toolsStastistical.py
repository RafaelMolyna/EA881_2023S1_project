import numpy as np
import matplotlib.pyplot as plt


def normal(x, u=0, v=1):
    return np.exp(-((x - u)/v)**2 / 2) / (np.sqrt(2 * np.pi) * v)


def integral(x, y):
    y = (y[0:-1] + y[1:]) / 2
    x = x[1:] - x[0:-1]
    result = np.cumsum(x * y)
    return np.concatenate([np.array([0]), result])


def generateCustomDistr(f, start=0, end=1, desloc=0):
    # x as a linear space with 10k points per unit
    x = np.linspace(start, end, int(1e4)*(end - start) + 1)
    y = f(x)
    yS = integral(x, y)

    mapfunc = (yS - yS[0]) / (yS[-1] - yS[0])

    def distr(n):
        if n > 1:
            r = np.random.rand(int(n))
        else:
            r = np.random.rand()
        return np.interp(r, mapfunc, x) + desloc

    return distr


def findErrProb(f1, f2):
    x1, y1 = f1
    x2, y2 = f2
    xInit = max(x1[0], x2[0])
    xEnd = min(x1[-1], x2[-1])
    x = np.linspace(xInit, xEnd, int(1e3) + 1)
    y1 = np.interp(x, x1, y1)
    y2 = np.interp(x, x2, y2)

    # calculate the error probability:
    err = np.trapz(np.minimum(y1, y2), x)

    # find the crossings:
    f = y1 - y2
    roots = np.diff(np.sign(f))
    indexRoots = np.nonzero(roots)
    crossings = [(x[i]*abs(f[i]) + x[i+1]*abs(f[i+1])) /
                 (abs(f[i]) + abs(f[i+1])) for i in indexRoots]

    return [err, crossings]


# test code as main:
if __name__ == '__main__':

    def f(x):
        return x*(1-x)

    squareDistr = generateCustomDistr(f)
    d = squareDistr(1e6)
    plt.hist(d, bins=100)
    plt.show()
