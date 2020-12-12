#link problem : https://leetcode.com/problems/defanging-an-ip-address/#
class Solution:
    def defangIPaddr(self, address):
        s = ""
        for i in range(len(address)) :
            if address[i] ==".":
                s+="[.]"
            else:
                s+=address[i]
        print(s)
        return s 
x = input()
ss =  Solution()
ss.defangIPaddr(x)
