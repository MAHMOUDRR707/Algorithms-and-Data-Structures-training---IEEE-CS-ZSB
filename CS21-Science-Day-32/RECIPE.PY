#problem  link : https://www.codechef.com/problems/RECIPE
#time :  O(n)


n = int(input())
for i in range(n):
    z = list(map(int,input().split()))
    x = z.pop(0)
    y = min(z)
    v = [i for i in range(len(z))  if z[i]%y == 0 ]
    if len(v)!= len(z) :
        print(*z)
    else :
       m = [ int(z[i]/y) for i in range(len(z))  ]
       print(*m)
