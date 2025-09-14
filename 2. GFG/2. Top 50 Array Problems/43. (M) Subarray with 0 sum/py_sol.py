#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        """
        Optimized: prefix-sum + hash set
        Time:  O(n)     – single pass
        Space: O(n)     – set of seen prefix sums
        Return: True if any zero-sum subarray exists, else False
        """
        seen = set()      # stores prefix sums we've seen so far
        s = 0             # running prefix sum
        for x in arr:
            s += x
            # zero-sum exists if: current element is 0, or prefix sum is 0,
            # or this prefix sum has been seen before
            if x == 0 or s == 0 or s in seen:
                return True
            seen.add(s)
        return False