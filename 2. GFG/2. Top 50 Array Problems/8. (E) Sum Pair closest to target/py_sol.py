class Solution:
    def sumClosest(self, arr, target):
        """
        Return the pair [a, b] (a <= b) whose sum is closest to target.
        Tie-break: if multiple are equally close, pick the pair with
                    larger |a - b|.
        If no pair exists (n < 2), return [].

        Time:  O(n log n) due to sorting
        Space: O(1) extra (ignoring output)
        """
        n = len(arr)
        if n < 2:
            return []

        arr.sort()  # O(n log n)

        i, j = 0, n - 1
        best_pair = []
        best_diff = float('inf')   # difference in sum from target
        best_gap  = -1             # |a - b| to resolve ties

        while i < j:
            a, b = arr[i], arr[j]
            s = a + b
            diff = abs(s - target)
            gap  = b - a           # arr sorted ⇒ b >= a

            # Update if strictly better, or tie with larger |a-b|
            if (diff < best_diff) or (diff == best_diff and gap > best_gap):
                best_diff = diff
                best_gap  = gap
                best_pair = [a, b]

            # Move pointers toward the target
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                # s == target -> perfect; still continue to respect tie-break
                # but typical early exit is fine if tie-break doesn't matter.
                # We'll adjust both sides to look for wider gap at same diff=0.
                i += 1
                j -= 1

        return best_pair