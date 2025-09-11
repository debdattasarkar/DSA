#User function Template for python3

class Solution:
    def getPairs(self, arr):
        """
        Return all unique pairs [x, y] such that x + y == 0.
        Requirements satisfied:
          - Each pair sorted (x <= y).
          - Pairs are unique (skip duplicates).
          - Output list sorted by the first element (thanks to sorting + two pointers).

        Time:  O(n log n) due to sorting
        Space: O(1) extra (ignoring output), since we sort in-place or on a copy
        """
        if not arr:
            return []

        arr.sort()                    # O(n log n)
        i, j = 0, len(arr) - 1
        ans = []

        while i < j:
            s = arr[i] + arr[j]
            if s < 0:
                i += 1                # need a bigger sum
            elif s > 0:
                j -= 1                # need a smaller sum
            else:
                # s == 0 -> record a unique pair
                ans.append([arr[i], arr[j]])

                # skip duplicates of arr[i]
                left_val = arr[i]
                while i < j and arr[i] == left_val:
                    i += 1

                # skip duplicates of arr[j]
                right_val = arr[j]
                while i < j and arr[j] == right_val:
                    j -= 1

        return ans