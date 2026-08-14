class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        left =1
        right = n
        while left <= right:
            mid = (left+right) // 2
            square = mid*mid
            if square == n:
                return True
            elif square < n:
                left = mid +1
            else:
                right = mid -1
        return False