class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left<= right:
            mid = (left+right)//2
            mid_val = nums[mid]
            if nums[mid] == target:
                return True
            left_val = nums[left]
            right_val = nums[right]
            if (nums[left] == nums[mid]== nums[right]):
                left +=1
                right -=1
                continue
            if nums[left] <= nums[mid]:
                if nums[left]<= target<= nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[right]>=target>=nums[mid]:
                    left = mid+1
                else:
                    right = mid -1
        return False

