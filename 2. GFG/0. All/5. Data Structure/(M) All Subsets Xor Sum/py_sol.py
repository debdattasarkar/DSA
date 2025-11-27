class Solution:
    def subsetXORSum(self, arr):
        """
        Optimized solution using bitwise properties.

        Idea:
        -----
        - For each bit position, consider whether at least one element has that bit set.
        - If no element has the bit, it never appears in any subset XOR contribution.
        - If at least one element has the bit set:
              -> This bit appears as '1' in exactly 2^(n-1) subset XORs.
        - So the total sum over all subsets equals:
              (bitwise OR of all elements) * 2^(n-1)

        Implementation Steps:
        ---------------------
        1) Compute bitwise OR of all values in arr.
        2) Compute factor = 1 << (n - 1).
        3) Return OR_value * factor.

        Time Complexity:
            O(n)  - single pass to compute OR.
        Space Complexity:
            O(1)  - just a few integer variables.
        """
        n = len(arr)

        # Step 1: Compute OR of all elements
        or_all = 0
        for value in arr:        # O(n)
            or_all |= value      # O(1) per step

        # Step 2: Each set bit contributes in exactly 2^(n-1) subsets
        factor = 1 << (n - 1)    # 2^(n-1)

        # Step 3: Final answer
        return or_all * factor