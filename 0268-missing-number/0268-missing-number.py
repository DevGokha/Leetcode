class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # f={}
        # for num in nums:
        #     f[num] = f.get(num, 0) + 1
        # for i ,
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
           
        return i+1
