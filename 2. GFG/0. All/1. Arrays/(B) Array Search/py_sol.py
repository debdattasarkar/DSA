class Solution:
    def search(self,arr, x):
        #code here
        """
        Perform linear search to find the first occurrence of x in arr.

        Time Complexity: O(n) - traverses the array once
        Space Complexity: O(1) - constant space used
        """
        for i in range(len(arr)):  # O(n)
            if arr[i] == x:        # O(1)
                return i           # first match found
        return -1                  # not found