import numpy as np
import matplotlib.pyplot as plt
import math
shape = (100, 100)
Lx = shape[0]
Ly = shape[1]

# Spin block
block = np.random.random(size=shape)
for i in range(shape[0]):
        for j in range(shape[1]):
            block[i][j]=0
# J/(kT)
Jcp = 0.01


def metropolis(b):
    for i in range(shape[0]):
        for j in range(shape[1]):
            temp = np.random.random()
            bij = b[i][j]
            de = (
                        math.cos(2 * math.pi * (b[(i + Lx + 1) % Lx][j] - bij)) +
                        math.cos(2 * math.pi * (b[(i + Lx - 1) % Lx][j] - bij)) +
                        math.cos(2 * math.pi * (b[i][(j + Ly + 1) % Ly] - bij)) +
                        math.cos(2 * math.pi * (b[i][(j + Ly - 1) % Ly] - bij)) -
                        math.cos(2 * math.pi * (b[(i + Lx + 1) % Lx][j] - temp)) -
                        math.cos(2 * math.pi * (b[(i + Lx - 1) % Lx][j] - temp)) -
                        math.cos(2 * math.pi * (b[i][(j + Ly + 1) % Ly] - temp)) -
                        math.cos(2 * math.pi * (b[i][(j + Ly - 1) % Ly] - temp))
                 )
            if np.random.random() < math.exp(-Jcp*de):
                b[i][j] = temp


plt.ion()
plt.show()

im = plt.imshow(block, cmap='hsv', vmin=0, vmax=1, interpolation='none')
t = 0
for i in range(10):
    metropolis(block)
    im.set_data(block)
    plt.draw()
    plt.pause(.0000001)
    t = t + 1
    print(t)
Jcp = 50
while True:
    metropolis(block)
    im.set_data(block)
    plt.draw()
    plt.pause(.0000001)
    t = t+1
    print(t)
