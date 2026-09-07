class Solution:
    def reverseWords(self, s: str) -> str:
        p = s.split()
        p.reverse()
        return " ".join(p)