#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        """
        Stable partition using extra buffer.
        Time  : O(n)  – two linear scans + one linear copy
        Space : O(n)  – temporary array to preserve order
        Modifies 'arr' in place as the driver expects (copies result back).
        """
        n = len(arr)
        tmp = []

        # Collect all non-negatives (>= 0) in order
        for x in arr:                 # O(n)
            if x >= 0:
                tmp.append(x)

        # Then collect all negatives in order
        for x in arr:                 # O(n)
            if x < 0:
                tmp.append(x)

        # Overwrite original array in place
        for i in range(n):            # O(n)
            arr[i] = tmp[i]