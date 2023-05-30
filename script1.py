import numpy as np
import matplotlib.pyplot as plt

r = np.random.rand(int(1e6))

# Mapping 1
d1 = r**2

# Mapping 2
c = r - 0.5
l = np.linspace(0, 1, int(1e3) + 1)
x = (l * 2 - 1) / 3**0.5
y = (x - x**3) * (3**1.5/4) + 0.5
d2 = np.interp(r, y, l)

# plt.plot(l, y)

# add plots
nBins = int(1e2)
plt.hist(d1 + 1, bins=nBins)
plt.hist(d2, bins=nBins)

# axis limits:
axis = plt.gca()
plt.xlim([0, 2])
plt.ylim([0, 5e4])

# add plot names:
plt.legend(['1/x^0.5', 'x^2'])

# show plot
plt.show()
