class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p= []
        n = []
        for num in nums:
            if num>=0:
                p.append(num)
            else:
                n.append(num)
        ans=[]
        for i in range(len(nums)):
            if i< len(p): ans.append(p[i])
            if i< len(n): ans.append(n[i])
        return ans
        