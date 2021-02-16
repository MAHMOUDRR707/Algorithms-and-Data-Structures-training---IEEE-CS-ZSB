#problem link : https://codeforces.com/contest/1195/problem/B
#time :  O(log n)


x,y = map(int,input().split())
z = 1
s = x
while(s>z):
    m = int((s+z)/2)
    if (((m*(m+1)/2)+(2+m-s))< y ) :
        z = m+1
    else :
        s = m
print(x-z)
