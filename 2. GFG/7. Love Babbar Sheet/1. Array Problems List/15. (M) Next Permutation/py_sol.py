class Solution:
    def nextPermutation(self, arr):
        """
        Rearranges arr into its lexicographically next permutation.
        If not possible (already the largest), rearranges to the lowest order.
        Time: O(n), Space: O(1) in-place
        """
        n = len(arr)
        if n <= 1:
            return arr  # trivial

        # 1) Find pivot: rightmost i with arr[i] < arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            # 2) Find rightmost successor > arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # 3) Swap pivot and successor
            arr[i], arr[j] = arr[j], arr[i]

        # 4) Reverse the suffix to get the smallest tail
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr  # returning arr for convenience (in-place anyway)