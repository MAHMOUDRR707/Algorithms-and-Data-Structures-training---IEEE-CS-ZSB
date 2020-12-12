#problem link :https://codeforces.com/contest/770/problem/A
#run time :  O(n)
import random
n,m = map(int,input().split())
z = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
 print(z[i%m],end="")
    
