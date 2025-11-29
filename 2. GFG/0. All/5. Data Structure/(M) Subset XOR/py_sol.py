class Solution:
    def subsetXOR(self, n : int):
        # Step 1: compute XOR of all numbers from 1 to n using n % 4 pattern
        remainder = n % 4
        if remainder == 0:
            xor_1_to_n = n
        elif remainder == 1:
            xor_1_to_n = 1
        elif remainder == 2:
            xor_1_to_n = n + 1
        else:  # remainder == 3
            xor_1_to_n = 0

        # Step 2: if XOR(1..n) == n, we can take all numbers
        if xor_1_to_n == n:
            # return [1, 2, ..., n]
            return [value for value in range(1, n + 1)]

        # Step 3: otherwise, drop exactly one element x such that:
        # XOR(1..n without x) = n
        # x = xor_1_to_n ^ n
        element_to_remove = xor_1_to_n ^ n

        # Step 4: build the subset skipping this element
        result_subset = []
        for value in range(1, n + 1):
            if value != element_to_remove:
                result_subset.append(value)

        # This subset has size n-1 and XOR exactly n.
        # It is unique for this size, so automatically lexicographically smallest.
        return result_subset