class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr: List[int], left: int, right: int) -> None:
        if left >= right:
            return
            
        mid = (left + right) // 2
        
       
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        
        
        self.merge(arr, left, mid, right)

    def merge(self, arr: List[int], left: int, mid: int, right: int) -> None:
        
        left_part = arr[left : mid + 1]
        right_part = arr[mid + 1 : right + 1]
        
        i = 0  
        j = 0  
        k = left  
        
        
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            
        
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            
       
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1