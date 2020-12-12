#problem link :https://codeforces.com/problemset/problem/767/A
# runt time : O(n)

n = int(input())
s = list(map(int,input().split()))
zz = [0] * n
for i in s:
    zz[int(i)-1] = i
    while zz[n-1] and n != 0:
        print(n, end=" ")
        n -= 1
    print("")
