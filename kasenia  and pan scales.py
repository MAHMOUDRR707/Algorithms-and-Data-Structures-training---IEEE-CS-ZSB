#problem link : http://codeforces.com/contest/382/problem/A 

m =  input()
z =  input()
x = m.index("|")
m1 = m[:x]
m2 = m[x+1:]
w1 = max(len(m1),len(m2))
w2 = min(len(m1),len(m2))
x1 = x
x2 = len(m)-x1-1
if len(m1)==len(m2)  or (w2+len(z)!=w1 and len(z)< w1) :
    print("Impossible")
else :
 for i in range(len(z)):
    if x1>x2 :
        m+=z[i]
        x2+=1
        
    else :
        m=z[i]+m
        x1+=1
        
 print(m)
