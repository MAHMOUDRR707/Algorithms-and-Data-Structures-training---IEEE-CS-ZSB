#problem link : https://codeforces.com/problemset/problem/268/B#
#time : O(n)

n =  int(input())
s =  0
for i in range(1,n):
    s+= (n-i)*i
print(s+n)
