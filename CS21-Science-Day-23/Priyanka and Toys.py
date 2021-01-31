#problem link: https://www.hackerrank.com/challenges/priyanka-and-toys/problem
#time: O(n)


def toys(w):
    x = min(w)
    k=0
    w = set(w)
    while(len(w)>0):
        k+=1
        x =  min(w)
        w = w.difference(set(range(x,x+5)))
    return k
n = int(input())

w = list(map(int, input().rstrip().split()))

result = toys(w)
print(result)
