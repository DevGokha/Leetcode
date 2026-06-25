class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        max_c = 0
        for i in range(n):
            if nums[i] == 1:
                count +=1
                max_c = max(max_c , count)
            else:
                count = 0

        return max_c
                 
                  
            

        
        