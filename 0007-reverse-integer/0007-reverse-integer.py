class Solution(object):
    def reverse(self, x):
     rev = int(str(abs(x))[::-1])
     
     if x<0:
        rev =-rev
     if rev < -(2**31)or rev > 2**31-1:
        return 0  

     return rev 