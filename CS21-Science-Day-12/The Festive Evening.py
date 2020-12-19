#problem link : https://codeforces.com/problemset/problem/834/B
#time : O(n)


n,m = map(int,input().split())
l = input()
z = {}
x = 0
for i in l :
   y = z.keys()
   if i in y :
       z[i] +=1
   else:
        z[i] = 1
zz= {}
for j in set(l) :
    zz[j]= 0
for  i in l:
    
        if zz[i] == 0 :
            if m == 0:
                x+=1
                break
            m-=1
            zz[i]+=1
        z[i]-=1
        if z[i] == 0:
                m+=1
            zz[i]=0
if x  :
    print("YES")
else :
    print("NO")
    
