class Solution:
    def rearrange(self, arr):
        """
        Builds a helper list, then copies back.
        Time:  O(n log n) due to sorting
        Space: O(n) extra for the helper
        """
        n = len(arr)
        if n <= 1:
            return

        arr.sort()  # O(n log n)
        left, right = 0, n - 1
        out = []

        # Alternate: max, min, max, min...
        take_max = True
        while left <= right:
            if take_max:
                out.append(arr[right])  # next max
                right -= 1
            else:
                out.append(arr[left])  # next min
                left += 1
            take_max = not take_max

        # Copy back in-place (problem says modify original)
        arr[:] = out