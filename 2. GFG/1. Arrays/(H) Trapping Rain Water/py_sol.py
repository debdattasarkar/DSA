from collections import deque

class Solution:
    def maxWater(self, arr):
        # Get length of input array
        n = len(arr)
        
        # Initialize stack to store indices of bars
        stack = deque()
        
        # Variable to accumulate total trapped water
        out = 0
        
        # Iterate over each block
        for i in range(n):
            # While stack is not empty and current height is greater than top of stack
            while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                # Pop the top element (this is the bottom of the water container)
                lower_height = arr[stack[-1]]
                stack.pop()

                # If stack becomes empty, no left boundary exists
                if len(stack) == 0:
                    break

                # Now the stack's new top is the left boundary
                left = stack[-1]
                
                # Width between left and right boundary, minus the bottom block
                dist = i - left - 1

                # Height of water is limited by the shorter of the two walls
                bounded_height = min(arr[i], arr[left]) - lower_height

                # Water volume = width * bounded_height
                out += dist * bounded_height

            # Push current index onto the stack
            stack.append(i)

        # Return the total trapped water
        return out
