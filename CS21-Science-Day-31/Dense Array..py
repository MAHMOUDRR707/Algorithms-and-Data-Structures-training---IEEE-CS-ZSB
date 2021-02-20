#problem link : https://codeforces.com/contest/1490/problem/A
#time : O(n*2 log2(n))

n =  int(input())
for i in range(n):
    m =  int(input())
    y = 0
    x =  list(map(int,input().split()))
    for j in range(1,m):
        m1 = max(x[j],x[j-1])
        m2 = min(x[j],x[j-1])
        if (m1 >= (2*m2)):
          while(m1 > 2*m2):
            m2*=2
            y+=1
    print(y)
        
