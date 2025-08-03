#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack = []

        for c, r in zip(color, radius):
            if stack and stack[-1] == (c, r):
                # Found a matching consecutive pair; remove it
                stack.pop()
            else:
                # Otherwise, push the current ball
                stack.append((c, r))

        # Remaining balls count is the size of the stack
        return len(stack)