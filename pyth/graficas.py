import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


data = collections.deque([0]*100, maxlen=100)
data2 = collections.deque([0]*100, maxlen=100)
data3 = collections.deque([0]*100, maxlen=100)

def data_gen():
    for k in range(100):
        t=k/100
        yield 0.5*np.sin(40*t)*np.exp(-2*t)

def data_gen2():
    for k in range(100):
        t=k/100
        yield 0.5*np.sin(60*t)

def data_gen3():
    for k in range(100):
        t=k/100
        yield 0.5*np.cos(60*t)

fig = plt.figure()
ax = plt.axes()
ax.set_title('Signal')
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_xlim(0,100)
ax.set_ylim(-1,1)
lines = ax.plot([], [])[0]
fig2 = plt.figure()
ax2 = plt.axes()
ax2.set_title('Signal2')
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")
ax2.set_xlim(0,100)
ax2.set_ylim(-1,1)
lines2 = ax2.plot([], [])[0]
fig3 = plt.figure()
ax3 = plt.axes()
ax3.set_title('Signal3')
ax3.set_xlabel("Time")
ax3.set_ylabel("Amplitude")
ax3.set_xlim(0,100)
ax3.set_ylim(-1,1)
lines3 = ax3.plot([], [])[0]

def animate(values):
    value=values
    data.append(value)
    lines.set_data(range(0,100),data)
    return lines

def animate2(values):
    value=values
    data2.append(value)
    lines2.set_data(range(0,100),data2)
    return lines2

def animate3(values):
    value=values
    data3.append(value)
    lines3.set_data(range(0,100),data3)
    return lines3


anim = animation.FuncAnimation(fig, animate, data_gen, interval=5)
anim2 = animation.FuncAnimation(fig2, animate2, data_gen2, interval=5)
anim3 = animation.FuncAnimation(fig3, animate3, data_gen3, interval=5)
plt.show() 