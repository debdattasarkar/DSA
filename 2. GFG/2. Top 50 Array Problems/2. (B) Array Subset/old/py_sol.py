#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freq = Counter(a)  # Count frequencies of a[]

        for num in b:
            if freq[num] == 0:
                return False  # Not found or exhausted
            freq[num] -= 1  # Use one occurrence
        
        return True