class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = -1
        ans =0
        for num in nums:
            digit = [int(d) for d in str(num)]
            digit_range = max(digit) - min(digit)
            if digit_range > max_range:
                max_range = digit_range
                ans = num
            elif digit_range == max_range:
                ans += num

        return ans
        

