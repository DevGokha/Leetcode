class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        o = x
        r =0
        while x>0:
            digit = x%10
            r = r*10 +digit
            x//=10
        return o == r
        