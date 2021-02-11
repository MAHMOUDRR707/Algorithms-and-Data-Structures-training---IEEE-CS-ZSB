#problam link : https://codeforces.com/contest/1476/problem/A
#time : O(n)
n = int(input())
for i in range(n):
    a,b =  map(int,input().split())
    x = int((a+b-1)/b)
    b *= x
    print(int((a+b-1)/a))
