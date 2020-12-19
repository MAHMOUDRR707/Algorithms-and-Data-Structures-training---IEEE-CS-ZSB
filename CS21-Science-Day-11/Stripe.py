#problem  link :https://codeforces.com/contest/18/problem/C 
#time  : O(n)

n = int(input())
z =  list(map(int,input().split()))
x = 0
xx = 0
total =  sum(z)
for i in range(1,n):
    xx+=z[i-1]
    if ((total-xx) == xx) :
        x+=1
print(x)
