#problem link : https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
#time :  O(n)



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    x = [[0,0,0]]
    sticks = sorted(sticks)
    for i in range(len(sticks)-2):
        z = list(sticks[i:i+3])
        if z[0]+z[1]>z[2]:
          if sum(z)>sum(x[0]):
            x = []
            x.append(z)
          else:
            continue
        
    if x[0]==[0,0,0]:
        return [-1]
    else:
        return x[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
