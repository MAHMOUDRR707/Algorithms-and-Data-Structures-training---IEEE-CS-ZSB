#problem link : https://codeforces.com/problemset/problem/467/B
#time :  O(n*2)


def count(n) :
    s = 0
    while (n!=0):
        n = n&(n-1)
        s +=1
    return s 


n,m,k = map(int,input().split())
z = []
for i in range(m+1):
    z.append(int(input()))
r = 0
c = 0
for i in range(m):
    r = z[i]^z[m]
    if( count(r)<= k):
        c+=1

print(c)
