class Solution:
    def check(self, nums: List[int]) -> bool:
        t = len(nums)
        count = 0
        for i in range(t):
            if nums[i] > nums[(i + 1) % t]:
                count += 1
        if count <= 1:
            return True
        else:
            return False
