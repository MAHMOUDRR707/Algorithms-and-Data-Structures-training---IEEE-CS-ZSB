n = int(input())
s = input()

if n == 1 :
    print( "Yes")
else :
     x = 0
     s = sorted(s)
     for i in range(1,n):
      if s[i] ==  s[i-1]:
         print ("Yes")
         x = 1
         break 
     if x == 0 :
          print("No")

