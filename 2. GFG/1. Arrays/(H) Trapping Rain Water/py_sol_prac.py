from collections import deque

class Solution:
    def maxWater(self, arr):
        # code here
        # Two pointer + stack
        n = len(arr)
        stack = deque()
        out = 0
        for i in range(n):
            while len(stack) > 0 and arr[i] > arr[stack[-1]] :
                lower_height = arr[stack[-1]]
                stack.pop()
                if len(stack) == 0:
                    break
                upper_height = min(arr[i], arr[stack[-1]])
                dist = i - stack[-1] - 1 
                out += dist * (upper_height - lower_height)
            stack.append(i)
        return out