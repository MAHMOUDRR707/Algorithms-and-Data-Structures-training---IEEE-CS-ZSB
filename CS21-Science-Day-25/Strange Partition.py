#problem link : https://codeforces.com/contest/1471/problem/A
#time : O(n**2)


n =  int(input())
for i in range(n):
    m,k =  map(int,input().split())
    s1 = 0
    s2 = 0
    x = list(map(int,input().split()))
    for i in range(m): 
        s1 +=int(((x[i])+k-1)/k)
        s2 += int(x[i])
    s2 =  int((s2+k-1)/k)
    print(s2,s1)
        
