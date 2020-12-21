#problem link : https://codeforces.com/contest/816/problem/B
#time : O(n)


n,k,q = map(int,input().split())
z = [0]*200000
z2 = [0] * 200000
for i in range(n):
    a,b = map(int,input().split())
    z[a]+=1
    z[b+1]-=1
for i in range(len(z)):
    z[i] +=z[i-1]
for i in range(len(z)):
    if z[i] >= k :
        z2[i] = 1
    else:
        z2[i] = 0
for i in range(len(z)):
    z2[i] +=z2[i-1]
for i in range(q):
    c,d = map(int,input().split())
    print(z2[d]-z2[c-1])
