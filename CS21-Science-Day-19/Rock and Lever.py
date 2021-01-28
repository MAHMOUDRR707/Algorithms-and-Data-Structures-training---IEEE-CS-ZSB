#problem link : https://codeforces.com/problemset/problem/1420/B
#time : O(n**3)




n = int(input())
x = 0
for i in range(n):
    m =  int(input())
    z = list(map(int,input().split()))
    for j in range(len(z)):
        for k in range(j+1,len(z)):
            if z[j]&z[k]>= z[j]^z[k]:
                x+=1
    print(x)
    x =0
        
