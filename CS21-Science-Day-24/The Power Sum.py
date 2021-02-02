#problem link:https://www.hackerrank.com/challenges/the-power-sum/problem
#time :o(n**2)



n=  int(input())
m =  int(input())
y =  int((n)**(1/m))
z = [1]+[0]*n

for i in range(1,y+1):
    s = i**m
    for j in range(n,s-1,-1):
       z[j]+=z[j-s]
print(z[-1])
