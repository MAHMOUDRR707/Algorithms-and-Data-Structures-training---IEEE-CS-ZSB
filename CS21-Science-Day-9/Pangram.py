#problem link :  https://codeforces.com/problemset/problem/520/A
#time  :  O(1)

n = int(input())
s =  input()
s = s.lower()
s =set(s)
if len(s) == 26 :
    print("YES")
else :
    print("NO")
