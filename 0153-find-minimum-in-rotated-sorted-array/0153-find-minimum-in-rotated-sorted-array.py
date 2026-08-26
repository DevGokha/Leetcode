class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums)-1
        # mid = (left+right)//2
            
        # return nums[mid+1]
        nums.sort()
        return nums[0]
