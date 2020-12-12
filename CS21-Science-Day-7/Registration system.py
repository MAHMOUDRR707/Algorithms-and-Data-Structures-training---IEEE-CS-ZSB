#problem link  : https://codeforces.com/contest/4/problem/C
# run time  O(n**2)

n = int(input())
z = {}
for i in range(0, n):
    s = input()
    if s in z:
        print(s+str(z[s]))
        z[s] += 1
    else:
        print("OK")
        z[s] = 1
