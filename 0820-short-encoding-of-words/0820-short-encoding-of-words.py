class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for i in range(1,len(word)):
                good.discard(word[i:])
        ans =0
        
        for word in good:
            ans += len(word) + 1
        return ans