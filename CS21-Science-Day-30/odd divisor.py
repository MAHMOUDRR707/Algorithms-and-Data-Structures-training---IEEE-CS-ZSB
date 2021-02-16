#problem link : https://codeforces.com/problemset/problem/1475/A
#time :  O(n)


n =  int(input())
for i in range(n):
    m = int(input())
    if m%2 != 0 and m > 1 :
        print("yes")
    else:
        print("no")
