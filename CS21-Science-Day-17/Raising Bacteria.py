c= 0
x = int(input())
x *=2
while(x!=0):
    c += x%2
    x //=2

print(int(c))
