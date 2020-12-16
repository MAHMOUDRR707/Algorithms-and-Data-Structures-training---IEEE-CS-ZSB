#problem link : https://codeforces.com/problemset/problem/368/B
#time :
a,b =  map(int,input().split())
z = list(map(int,input().split()))
x = set()
y = []
for  i  in range(a,0,-1):
    x.add(z[i-1])
    y.append(len(x))
for i in range(b):
    print(y[-1*int(input())])
