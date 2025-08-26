class Solution:
    def countTriangles(self, arr):
        # code here
        """
        Optimized two-pointer after sorting.
        Time:  O(n^2)   -- dominant double loop after sort
        Space: O(1)     -- in-place calculations
        """
        n = len(arr)
        if n < 3:
            return 0

        arr.sort()  # O(n log n)
        count = 0

        # Fix the largest side at position k, scan i..j for pairs
        for k in range(n - 1, 1, -1):   # k from n-1 down to 2
            i, j = 0, k - 1
            while i < j:
                # if smallest + second-largest > largest, then
                # (i, i+1, ..., j-1, j) all with this j form valid triangles
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)
                    j -= 1  # try a smaller middle to see if more pairs exist
                else:
                    i += 1  # sum too small; increase the smaller side

        return count