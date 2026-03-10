class Solution:
    def countSubarrays(self, arr):
        # code here
        n = len(arr)
        next_smaller_index = [n] * n  # default: no smaller element
        stack = []  # monotonic increasing stack
        
        # Step 1: Compute Next Smaller Element (NSE)
        for i in range(n - 1, -1, -1):
            # Maintain increasing stack
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            # If stack not empty, top is next smaller
            if stack:
                next_smaller_index[i] = stack[-1]
            
            stack.append(i)
        
        # Step 2: Count valid subarrays
        total_valid = 0
        for i in range(n):
            total_valid += next_smaller_index[i] - i
        
        return total_valid

