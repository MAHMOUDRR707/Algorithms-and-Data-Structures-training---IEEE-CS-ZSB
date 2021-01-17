problem link :  https://www.hackerrank.com/challenges/sam-and-substrings/problem
time  :  O(n) 



s = input().strip()
size = len(s)
prev = int(s[0])
MOD  =  10**9+7
total = prev
for i in range (1, size):
    total= (total*10+int(s[i])*(i+1))%(MOD)
    prev = (total+prev)%(MOD)
print(prev)
