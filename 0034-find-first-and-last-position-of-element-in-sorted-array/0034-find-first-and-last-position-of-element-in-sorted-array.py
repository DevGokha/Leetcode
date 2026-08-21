class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def dev(is_first: bool) -> int:
            left = 0
            right =len(nums)-1
            arr = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid]> target:
                    right =mid-1
                else:
                    arr = mid
                    if is_first:
                        right = mid-1
                    else:
                        left = mid+1
            return arr
        return [dev(True),dev(False)]
            
        
