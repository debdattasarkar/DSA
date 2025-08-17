class Solution:
    def rearrange(self, arr, x):
        # code here
        # Time: O(n log n) due to sort
        # Space: O(1) extra if sorting in place (Python's Timsort is in-place); otherwise O(n).
        # Python's sort is stable, so ties keep original order automatically.
        arr.sort(key=lambda a: abs(a - x))
        return arr