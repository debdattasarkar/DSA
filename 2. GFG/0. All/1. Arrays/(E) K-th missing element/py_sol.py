# User function Template for python3

class Solution:
    def KthMissingElement(self, arr, k):
        """
        Linear scan across gaps between consecutive elements.
        Time:  O(n)
        Space: O(1)
        Returns -1 if the k-th missing does not exist within [arr[0], arr[-1]].
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1

        for i in range(n - 1):
            gap = arr[i + 1] - arr[i] - 1  # how many integers are missing here
            if gap >= k:
                return arr[i] + k          # k-th missing lies in this gap
            k -= gap                       # otherwise consume this gap and move on

        return -1                           # not enough missing numbers
