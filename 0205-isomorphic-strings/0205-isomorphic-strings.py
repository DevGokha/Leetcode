class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for cs, ct in zip(s, t):
            if cs in mt and mt[cs] != ct:
                return False
            if ct in ms and ms[ct] != cs:
                return False
            ms[ct] = cs
            mt[cs] = ct
        return True
        