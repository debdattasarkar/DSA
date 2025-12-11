from typing import List
import math

def original_length_from_pairs(pair_count: int) -> int:
    """
    Given m = number of pair sums, solve n(n-1)/2 = m for n.

    n^2 - n - 2m = 0 -> n = (1 + sqrt(1 + 8m)) / 2

    We assume input is valid so the result is an integer.
    """
    if pair_count == 0:
        return 1  # if no pair sums, original could be length 1
    disc = 1 + 8 * pair_count
    root = math.isqrt(disc)
    # In valid test cases, root*root == disc
    return (1 + root) // 2
    
class Solution:
    def constructArr(self, arr):
        """
        Optimized O(n) solution to reconstruct one valid original array
        from its pair-sum array.

        Steps:
            1) Determine n (original length) from m = len(arr) using:
                   n = (1 + sqrt(1 + 8m)) / 2
            2) Handle small cases n = 1, 2.
            3) Use first three relevant pair sums for n >= 3:
                   S01 = r0 + r1     = arr[0]
                   S02 = r0 + r2     = arr[1]
                   S12 = r1 + r2     = arr[n-1]
               Derive:
                   r0 = (S01 + S02 - S12) / 2
                   r1 = S01 - r0
                   r2 = S02 - r0
            4) For j >= 3:
                   arr[j-1] = r0 + rj  ->  rj = arr[j-1] - r0

        Time  : O(n) where n is original array length
        Space : O(n) to store the original array (no extra big structures)
        """
        m = len(arr)
        n = original_length_from_pairs(m)

        # n == 1: no pair sums; any 1-element array works
        if n == 1:
            return [0]

        # n == 2: only one pair r0 + r1 = arr[0],
        # choose e.g. r0 = 0, r1 = arr[0]
        if n == 2:
            return [0, arr[0]]

        # n >= 3:
        S01 = arr[0]       # r0 + r1
        S02 = arr[1]       # r0 + r2
        S12 = arr[n - 1]   # r1 + r2  (first pair in the second row)

        # Compute r0, r1, r2
        r0 = (S01 + S02 - S12) // 2
        r1 = S01 - r0
        r2 = S02 - r0

        original = [0] * n
        original[0] = r0
        original[1] = r1
        original[2] = r2

        # Compute remaining elements using sums with r0
        for j in range(3, n):
            # arr[j-1] stores r0 + rj
            original[j] = arr[j - 1] - r0

        return original