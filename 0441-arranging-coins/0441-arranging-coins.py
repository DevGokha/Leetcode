class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left+right) // 2
            coin =(mid* (mid+1) ) // 2
            if coin == n:
                return mid 
            elif coin < n:
                left = mid +1
            else:
                right = mid -1
        return right