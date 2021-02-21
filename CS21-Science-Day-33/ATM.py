#problem  link :https://www.codechef.com/problems/HS08TEST
#time : O(1)

m,n  = map(float,input().split())
if m> n :
    print(n)
elif m%5==0:
    print("{:0.2f}".format(n-m-0.5))
else:
    print("{:0.2f}".format(n))
