class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        for i in range(1, len(n)):
            n[i] = max(n[i], n[i]+n[i-1])
        return max(n)
         

