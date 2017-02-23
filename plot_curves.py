import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-3)*(x+2)*(x+3)
def g(x):
    return abs((x-1)*(x-1.5)*(x-2)*(x-3)*(x-4))

x = np.arange(1,4,0.1)
y1 = [f(k) for k in x]
y2 = [g(k) for k in x]

# compute the derivative of g
dy2 = np.diff(y2)
ddy2 = np.diff(dy2)

# first derivative
dy2 = (dy2[:-1] + dy2[1:])/2
x_dy2 = x[1:-1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()
lines1, = ax.plot(x,y2,label="g(x)")
# # plot first derivative
# lines2, = ax.plot(x_dy2,dy2,label="g'(x)")
# # plot second derivative
# lines3, = ax.plot(x_dy2,ddy2,label="g''(x)")
# # lengend
# plt.legend(handles=[lines1,lines2,lines3])
# axis limits
# ax.set_ylim([-1,1])
plt.show()
