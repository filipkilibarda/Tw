"""
Twitter puddle problem.
-------------------
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import math

def createMatrix(lst):
    height = max(lst)
    matrix = []
    for num in lst:
        row = [1]*height
        row[:num] = [0]*num
        matrix.append(row)
    newMatrix = [list(row) for row in zip(*matrix)]
    newMatrix = newMatrix[::-1]
    return newMatrix

def count_puddle(matrix):
    count=0
    for row in matrix:
        trim(row)
        count += sum(row)
    return count

def trim(row):
    while row[0]==1:
        del row[0]
    while row[-1]==1:
        del row[-1]

# lst = [4,5,0,0,6,6,7,8,1,1,1,3,3,3,2,2,2]
# matrix = createMatrix(lst)
# area_puddle = count_puddle(matrix)
# print("area of the puddle %s" % area_puddle)

# print("testing the version that can be plotted")
# print("----------------------------------------")
"""
Twitter puddle problem:

Version that can be plotted
"""
def create_puddles(matrix):
    for row in matrix:
        modify(row)

def modify(row):
    i=0
    while i < len(row):
        if row[i]==1:
            row[i] = -1
        else:
            break
        i+=1
    i=-1
    while i >= -len(row):
        if row[i]==1:
            row[i] = -1
        else:
            break
        i-=1

def f(x):
    from math import sin,cos,exp
    """
    Suggested domain: x in [0,5.5]
    """
    sin(x) + sin(2*x) + sin(3*x) + sin(4*x) + .02*sin(44*x) + .05*sin(54*x) + 4 - 2*exp(-(x-3)**2) + 2*exp(-(x-3.5)**2/.2) + 1.2*exp(-(x-1.8)**2/.2)
    return x

lst = [4,5,0,0,6,6,7,8,1,1,1,3,3,3,2,2,2]
# lst = [f(x) for x in np.arange(0,5.5,.2)]
matrix = createMatrix(lst)
create_puddles(matrix)

# lst = [0,1,2,1,1,2,3]
# matrix = createMatrix(lst)
# create_puddles(matrix)

# make a color map of fixed colors
cmap = colors.ListedColormap([
    "#ffffff",
    "#D4C26A",
    "#ffffff",
    # "#7788AA",
    ])
norm = colors.BoundaryNorm([-1.5,-.5,.5,1.5], cmap.N)
plt.imshow(matrix,cmap=cmap,norm=norm)
plt.axis("off")
plt.savefig("big_no_puddle.png",bbox_inches='tight',figsize=(2,2))
plt.show()

