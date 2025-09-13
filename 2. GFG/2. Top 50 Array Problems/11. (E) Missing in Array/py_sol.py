class Solution:
    def missingNum(self, arr):
        # Number of elements should be n - 1, so total n is:
        n = len(arr) + 1

        # Expected sum from 1 to n
        expected_sum = n * (n + 1) // 2  # Time: O(1), Space: O(1)

        # Actual sum of given elements
        actual_sum = sum(arr)  # Time: O(n), Space: O(1)

        # Missing number is the difference
        return expected_sum - actual_sum