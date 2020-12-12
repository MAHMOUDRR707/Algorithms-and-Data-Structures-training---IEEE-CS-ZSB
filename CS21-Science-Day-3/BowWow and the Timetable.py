#link problem : https://codeforces.com/contest/1204/problem/A

z = []
x = 1
import numpy as np
import math as mt
for i in range(1,101):
    z.append(x)
    x = x*2 
s =  input()
s = s[::-1]
y = 0
for i in range(len(s)) : 
    if s[i]=="1":
        y+=z[i]
w  = mt.log(y,4)
if w is int:
    print(w)
else : 
  print(int(np.ceil(w)))
