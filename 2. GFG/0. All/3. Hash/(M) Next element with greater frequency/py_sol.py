from collections import Counter
class Solution:
    def nextFreqGreater(self, arr):
        # Frequency of each number in the whole array
        freq = Counter(arr)
        
        n = len(arr)
        result = [-1] * n
        
        # Stack will store indices. We'll keep it such that
        # freq[arr[stack[-1]]] is strictly greater than freq of elements below it
        stack = []
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            current_frequency = freq[arr[i]]
            
            # Pop indices whose frequency is <= current_frequency
            # because they cannot be the "next greater frequency" for this i
            while stack and freq[arr[stack[-1]]] <= current_frequency:
                stack.pop()
            
            # Now the stack top (if exists) is the nearest to right with higher freq
            if stack:
                result[i] = arr[stack[-1]]
            else:
                result[i] = -1
            
            # Push this index for elements to the left
            stack.append(i)
        
        return result
        