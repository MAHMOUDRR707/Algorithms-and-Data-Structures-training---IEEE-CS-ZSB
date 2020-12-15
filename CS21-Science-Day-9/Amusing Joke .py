#problem link :https://codeforces.com/problemset/problem/141/A
#time :  O(n)


s = input()
s = s+input()
s1 = list(set(s))
x = input()
x1 = list(set(x))
z = {}
for i in range(len(s1)):
    z[s1[i]] =  s.count(s1[i])
zz ={}
for i in range(len(x1)):
    zz[x1[i]] = x.count(x1[i])
if zz ==z :
    print("YES")
else :
    print("NO")
    
    
