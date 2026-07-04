class Solution:
    def sortColors(self, nums: List[int]) -> None:
        noz =0
        noo=0
        notw =0
        for num in nums:
            if num == 0: noz +=1
            elif num == 1: noo +=1
            else: notw +=1
        for i in range(len(nums)):
            if i<noz: 
                nums[i] =0
            elif i<noo+noz: 
                nums[i] = 1
            else: 
                nums[i] = 2
