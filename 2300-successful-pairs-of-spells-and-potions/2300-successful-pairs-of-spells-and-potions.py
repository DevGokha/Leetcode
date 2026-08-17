class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        answer =[]
        
        for s in spells:
            left = 0
            right = n
            while left< right:
                mid = (left+right)//2
                if s*potions[mid] >= success:
                    right = mid
                else:
                    left = mid +1
            answer.append(n-left)
        return answer


