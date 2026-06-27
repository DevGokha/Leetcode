class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a =sorted(t)
        b =sorted(s)
        for i in range(len(s)):
            if a[i] != b[i]:
                return False
        return True
        