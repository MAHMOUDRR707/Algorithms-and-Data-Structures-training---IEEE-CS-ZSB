#problem link : https://codeforces.com/problemset/problem/1199/B
#time : O(1)


a,b  = map(int,input().split())
print("{:.13f}".format(((b*b-a*a)/(2*b))))
