class Solution:
    def missingRange(self, arr, low, high):
        # Build a hash set for O(1) average membership checks
        # Time: O(n)
        # Space: O(n)
        present_values = set(arr)

        # Scan the full range and collect missing values
        # Time: O(high-low+1)
        # Space: O(k) for output list
        missing_numbers = []
        for value in range(low, high + 1):
            if value not in present_values:
                missing_numbers.append(value)

        return missing_numbers
