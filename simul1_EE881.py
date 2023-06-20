import numpy as np
import matplotlib.pyplot as plt
from toolsStastistical import generateCustomDistr, integral, normal, findErrProb
import random

# import asyncio as asy
# import time


def f1(x):
    return x*(3-x)


def f2(x):
    return np.minimum(x, 3-x)


def f3(x):
    return normal(x, 0, 0.5)


def createDistr(func, start=0, end=1, desl=0):
    x = np.linspace(start, end, 1001)
    y = func(x)
    S = np.trapz(y, x)
    # add x offset:
    x += desl
    # turn y_area = 1:
    y /= S
    # add zero points on the tail and the beginning:
    x = np.concatenate(([x[0]], x, [x[-1]]))
    y = np.concatenate(([0], y, [0]))
    plt.plot(x, y)
    # generate distribution:
    distr = generateCustomDistr(func, start, end, desl)

    return [distr, x, y]


d1, x1, y1 = createDistr(f1, 0, 3)
d2, x2, y2 = createDistr(f2, 0, 3, 2.5)
d3, x3, y3 = createDistr(f3, -3, 3, 6)

# symbols
H = [0, 1, 2]

# codes
C = [1, 4, 6]

# weights: Priors
w = np.array([2, 3, 2.5])
w = w / w.sum()

# add weights to distributions
y1 *= w[0]
y2 *= w[1]
y3 *= w[2]

# signal transmitter
channel = [d1, d2, d3]

# create msg to send:
sent_H = np.random.choice(H, 10000, p=w)

# turn H into Y (Ch with noise):
receivedMsg_Y = list(map(lambda x: channel[x](1), sent_H))


def guesser(v):
    '''
    guesser function as theory proposal (not optimized)
    '''
    return np.argmax([
        np.interp(v, x1, y1),
        np.interp(v, x2, y2),
        np.interp(v, x3, y3),
    ])


guessed_H = np.array(list(map(guesser, receivedMsg_Y)))


file_sent = '\n'.join([*map(lambda a: f'{a}', np.split(sent_H, 1000))])
file_received = '\n'.join([*map(lambda a: f'{a}', np.split(guessed_H, 1000))])

numErr = np.count_nonzero(guessed_H - sent_H)
porcErr = round(numErr / len(guessed_H) * 100, 1)
print(f'number of Errors: {numErr}, ~{porcErr} %')


# Create files for comparison:
file = open('file_sent.txt', 'w')
file.write(file_sent)
file.close()

file = open('file_received.txt', 'w')
file.write(file_received)
file.close()

err1, [[roots1]] = findErrProb([x1, y1], [x2, y2])
err2, [[roots2]] = findErrProb([x2, y2], [x3, y3])
print(f'error prob: {(err1 + err2)*100} %')
print(f'roots: {roots1}, {roots2}')

plt.xlim([0, 9])
plt.ylim([0, 0.9])
plt.legend(['distr1', 'distr2', 'distr3'])
plt.show()

# plt.show(block=False)
# plt.pause(10)
# plt.close()

plt.hist(receivedMsg_Y, bins=100)
plt.show()
