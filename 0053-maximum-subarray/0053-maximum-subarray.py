class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        d = n[0]
        m = n[0]

        for i in range(1,len(n)):
            d = max(n[i], d+n[i])
            m = max(m,d)
        return m

