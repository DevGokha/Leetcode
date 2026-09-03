class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        def canMake(day):
            flower= 0
            bouquet = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flower +=1
                    if flower == k:
                        bouquet +=1
                        flower =0
                else:
                    flower =0 
            return bouquet >= m
        left , right = min(bloomDay), max(bloomDay)
        while left< right:
            mid = (left+right)//2
            if canMake(mid):
                right = mid
            else:
                left = mid+1
        return left 