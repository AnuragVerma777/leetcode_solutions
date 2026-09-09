class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(s)-1
        while left < right:
              if s[left] == s[right]: 
               left +=1
               right -=1 
              else:
                return False
        return True    