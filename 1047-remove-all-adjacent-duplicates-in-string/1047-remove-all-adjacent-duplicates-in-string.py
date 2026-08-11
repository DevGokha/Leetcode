class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        n = len(s)

        for current in s:
            if stack and stack[-1] == current:
                stack.pop()
            else:
                stack.append(current)
        return "".join(stack)