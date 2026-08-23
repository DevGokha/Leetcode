class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p= []
        n = []
        
        for i in range(len(nums)):
            if nums[i] >=0:
                p.append(nums[i])
            else:
                n.append(nums[i])

        ans = []
        for i in range(len(nums)):
            if i < len(p): ans.append(p[i])
            if i< len(n): ans.append(n[i])
        return ans
        