#problem link : https://codeforces.com/contest/855/problem/A
#run time : O(n**2)
n = int(input())
z =[]
for i in range(n):
    s= input()
    
    if s in z :
        print("YES")
    else :
        print("NO")
    z.append(s)
    
