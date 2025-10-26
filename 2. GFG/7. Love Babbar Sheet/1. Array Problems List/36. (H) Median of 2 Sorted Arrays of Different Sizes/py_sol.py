class Solution:
    def medianOf2(self, a, b):
        """
        Median of two sorted arrays (possibly different sizes).
        Binary-search a partition on the smaller array.

        Time  : O(log(min(n, m)))
        Space : O(1)
        Returns a float median.
        """
        # Ensure 'a' is the smaller array to minimize the search space
        if len(a) > len(b):
            a, b = b, a

        n, m = len(a), len(b)
        if n == 0 and m == 0:
            raise ValueError("Both arrays are empty")

        total = n + m
        left_target = (total + 1) // 2  # size of left partition

        lo, hi = 0, n  # 'i' ranges from 0..n
        INF_POS = float('inf')
        INF_NEG = float('-inf')

        while lo <= hi:
            i = (lo + hi) // 2
            j = left_target - i

            a_left  = INF_NEG if i == 0 else a[i - 1]
            a_right = INF_POS if i == n else a[i]
            b_left  = INF_NEG if j == 0 else b[j - 1]
            b_right = INF_POS if j == m else b[j]

            # Valid partition?
            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return float(max(a_left, b_left))
                left_max = max(a_left, b_left)
                right_min = min(a_right, b_right)
                return (left_max + right_min) / 2.0

            # Need to shift 'i'
            if a_left > b_right:
                # too many from 'a' on the left, move left
                hi = i - 1
            else:
                # too few from 'a' on the left, move right
                lo = i + 1

        # Should never reach here if inputs are sorted and total > 0
        raise RuntimeError("No valid partition found")