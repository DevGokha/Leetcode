class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_f = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_f and char_f[char] >= left:
                left = char_f[char] +1
            char_f[char] = right
            max_len= max(max_len, right-left+1)
        return max_len




