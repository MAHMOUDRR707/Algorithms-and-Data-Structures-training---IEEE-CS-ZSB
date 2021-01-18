problem link : https://www.hackerrank.com/challenges/equal/problem
time :  O(n) 





#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    MIN = min(arr)
    ans = float('inf')
    for i in range(len(arr)):
        dec = MIN - i
        cur = sum([(n-dec)//5 + (n-dec)%5//2 + (n-dec)%5%2 for n in arr]
)
        ans = min(ans, cur)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
  
