 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        """
        Hash-set approach: Expand only from starts (x-1 not present).
        Time : O(n) average   (each element checked a constant number of times)
        Space: O(n)           (set of unique numbers)
        """
        if not arr:
            return 0
        
        values = set(arr)  # unique numbers; duplicates collapse
        
        best_len = 0
        for x in values:
            # Start of a consecutive run iff (x-1) is not present
            if (x - 1) not in values:
                y = x
                # Count upward while numbers are present
                while y in values:
                    y += 1
                # Run is [x, y-1] -> length:
                best_len = max(best_len, y - x)
        
        return best_len