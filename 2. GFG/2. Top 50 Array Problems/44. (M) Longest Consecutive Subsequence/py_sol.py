 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        """
        Hash-set start-detection.
        Time:  O(n) average (each element considered as start once; counting
               across the array happens at most n times total)
        Space: O(n) for the set
        """
        if not arr:
            return 0
        
        s = set(arr)          # O(n)
        best = 0
        
        for x in s:           # iterate unique values
            if x - 1 not in s:        # x is a potential start  → O(1) avg
                # count forward from x
                y = x
                while y in s:         # each y across all runs visited once
                    y += 1
                best = max(best, y - x)
        
        return best