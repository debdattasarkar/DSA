#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        # Calculate the lower and upper bounds for valid i
        low = max(1, q - n)
        high = min(n, q - 1)
        
        # Total valid pairs is high - low + 1 (only if range is valid)
        count = max(0, high - low + 1)
        
        return count