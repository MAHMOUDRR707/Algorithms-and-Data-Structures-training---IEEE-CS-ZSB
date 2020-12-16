#problem link :https://codeforces.com/problemset/problem/433/B
#time :O(n)
n =  int(input())
z =  list(map(int,input().split()))

x  = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    if a == 1 :
      
         print(sum(z[b-1:c]))
      
    else :
        if b == 1:
           if c-b != 1 :
               print(sum(z[b-1:c]))
           else :
               print(sum(z[b-1:c-1]))
        else :
            print(sum(z[b-1:c]) + z[b-3])
