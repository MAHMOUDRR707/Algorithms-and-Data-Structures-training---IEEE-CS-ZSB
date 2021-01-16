Problem link : https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?h_r=internal-search
time : O(n)


class queue(object):
    def __init__(self):
        self.items = []
    def Dequeue(self) :
        self.items.pop(0)
    def Enqueue(self,x):
        self.items.append(x)
    def print_(self):
        print(self.items[0])
n =  int(input())
z =  queue()
for i in range(n):
    x =  list(map(int,input().split()))
    if  x[0] == 1 :
        z.Enqueue(x[1])
    elif x[0] == 2 :
        z.Dequeue()
    else :
        z.print_()
        
