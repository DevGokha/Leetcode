class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in p:
                p[nums[i]] = i
            else:
                return[i,p[diff]]


