#problem link : https://coderbyte.com/editor/Find%20Intersection:Python3
#time :  O(n)


l =   input().split('", "')
l1 = l[0]
l2 =l[1]
l1 =  list(map(int,l1[1:len(l1)].split(", ")))
l2 =  list(map(int,l2[0:len(l2)-1].split(", ")))
x = [ i for i in l1  if i  in l2 ]
print(x)
