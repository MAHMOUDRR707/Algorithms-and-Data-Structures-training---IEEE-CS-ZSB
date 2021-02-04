#problem link : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
#time: O(n)



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    z = [0] *  max((n+1),4)
    z[1],z[2],z[3] = 1,2,4
    for i in range(4,n+1):
        z[i] = z[i-1]+ z[i-2 ] + z[i-3]
    return z[n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
