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

"""
A test
"""
lst = [4,5,0,0,6,6,7,8,1,1,1,3,3,3,2,2]
matrix = createMatrix(lst)
for row in matrix: print(row)
for row in matrix: print([" " if x==1 else "X" for x in row])
area_puddle = count_puddle(matrix)
print("area of the puddle is %s" % area_puddle)
