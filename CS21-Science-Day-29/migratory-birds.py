#problem link : https://www.hackerrank.com/challenges/migratory-birds/problem
#time :  O(n)

n = int(input())
z =  list(map(int,input().split()))
x = []
for i in range(1,6):
    x.append(z.count(i))
m = 0
y = x[0]
for i in x :
    if m < i :
        y = x[i]
        m = i
print(x[max(x)] ,y )
        
    
