class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        h = sorted(nums)
        p = h[-1]
        for i in range(len(nums)):
            if nums[i] == p:
                return i
