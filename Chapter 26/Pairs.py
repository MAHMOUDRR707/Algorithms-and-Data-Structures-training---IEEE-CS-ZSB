#problem link : https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
#time :  O(n**2) 



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, z):
    x =[]
    for i in range(len(z)):
      for j in range(i+1,len(z)):
        x.append(abs(z[i] - z[j]))
    return x.count(k)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
