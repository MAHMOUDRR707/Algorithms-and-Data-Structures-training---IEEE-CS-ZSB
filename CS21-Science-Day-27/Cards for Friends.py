#problem link : https://codeforces.com/contest/1472/problem/A
#time: O(n**2)
n = int(input())
z =[]
for i in range(n):
     x = 1
     h,w,m =  map(int,input().split())
     while( h%2 == 0 ):
         x*=2
         h/=2
     while(w%2==0):
        x*=2
        w/=2
     if(x>= m) :
        z.append("yes")
     else:
        z.append("no")
print(*z)
