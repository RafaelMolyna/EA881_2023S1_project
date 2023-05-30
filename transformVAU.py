import numpy as np
import random as rand
import matplotlib.pyplot as mplt

size = int(1e5) + 1
x = np.linspace(0, 1, num=size)[1:]
fx = np.ones(size)[1:]
fy = 1/(2 * np.sqrt(x))

areaX = np.trapz(fx, x=x)
areaY = np.trapz(fy, x=x)

print("prob total de x:", areaX)
print("prob total de y:", areaY)

# ploting:

# ax.plot(x, fy, linewidth=2.0)
# ax.set(xlim=(0, 1), xticks=np.arange(1, 10), ylim=(0, 1), yticks=np.arange(1, 10))
# ax.set(xlim=(0, 1), ylim=(0, 10),  yticks=np.arange(1, 10))

fig, ax = mplt.subplots()
ax.plot(x, fy)
ax.set(xlim=(0, 1), ylim=(0, 10))
mplt.show()


# random value [0,1):
rand.random()
# random value [0,100):
np.random.randint(100)
# random value [1,10]:
rand.randint(1, 10)

# random array [0,1): 50 samples
np.random.rand(50)
# random array [0,100): 15 samples
np.random.randint(100, size=15)
# random array [1,100): 15 samples
np.random.randint(1, 100, size=15)


x = np.random(int(1e5))
top = 2
m = x - 0.5
y = m**3 + 1/top * m + 0.5
