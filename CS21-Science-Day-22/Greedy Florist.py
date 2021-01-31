#!/bin/python3
#problem link : https://www.hackerrank.com/challenges/greedy-florist/problem
#time : O(n)



import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    s = 0 
    c = sorted(c,reverse=True)
    for i in range(len(c)):
        s+=((int(i/k)+1)*c[i])
    return s
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
 
