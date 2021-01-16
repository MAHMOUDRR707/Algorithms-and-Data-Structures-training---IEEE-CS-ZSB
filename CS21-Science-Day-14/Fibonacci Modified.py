problam link: https://www.hackerrank.com/challenges/fibonacci-modified/problem?h_r=internal-search
time  : O(n)


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    z = [t1,t2]
    for i in range(1,n-1):
        x = z[i-1] + z[i]*z[i]
        z.append(x)
    return z[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
