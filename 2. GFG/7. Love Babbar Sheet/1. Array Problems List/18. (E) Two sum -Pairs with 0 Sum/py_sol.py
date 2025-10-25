#User function Template for python3

class Solution:
    def getPairs(self, arr):
        """
        Return all unique pairs [x, y] with x + y == 0.
        Each pair [x, y] is sorted and the result list is sorted with no duplicates.

        Time:  O(n log n) due to sorting; two-pointer scan is O(n)
        Space: O(1) extra (ignoring output)
        """
        n = len(arr)
        if n < 2:
            return []

        arr.sort()  # sort ascending to enable two-pointer and easy de-dup
        left, right = 0, n - 1
        result = []

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == 0:
                # We found one unique pair
                result.append([arr[left], arr[right]])

                # Move left forward skipping duplicates of arr[left]
                left_val = arr[left]
                while left < right and arr[left] == left_val:
                    left += 1

                # Move right backward skipping duplicates of arr[right]
                right_val = arr[right]
                while left < right and arr[right] == right_val:
                    right -= 1

            elif current_sum < 0:
                # We need a larger sum -> move left forward
                left += 1
            else:
                # We need a smaller sum -> move right backward
                right -= 1

        return result