#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        """
        Use prefix sums: if any prefix repeats or becomes zero -> zero-sum subarray exists.
        Time:  O(n)    -- single pass
        Space: O(n)    -- set of seen prefix sums
        """
        seen_prefix = set()    # stores prefix sums we've seen so far
        running_sum = 0

        for x in arr:          # O(n)
            running_sum += x   # update prefix

            # Case 1: subarray from 0..i has sum 0
            # Case 2: some earlier prefix equals this prefix -> in-between sum 0
            if running_sum == 0 or running_sum in seen_prefix:
                return True

            seen_prefix.add(running_sum)  # remember this prefix for later

        return False  # no zero-sum subarray found