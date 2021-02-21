#problem link :https://www.codechef.com/problems/FLOW017
#time :  O(n)


n = int(input())
for i in range(n):
    z =  list(map(int,input().split()))
    z.pop(z.index(max(z)))
    print(max(z))
