class Solution:
    def cntWays(self, arr):
        """
        Optimized solution using prefix/suffix-like sums.

        Idea:
            - Precompute total sum of elements at even and odd indices.
            - Traverse array once, treating each index as "removed":
                * Subtract arr[i] from the appropriate right-side sum
                  (even or odd, based on i % 2).
                * After removal, the right side's parity flips:
                      new_even_sum = leftEvenSum + rightOddSum
                      new_odd_sum  = leftOddSum  + rightEvenSum
                * If new_even_sum == new_odd_sum, this index is valid.
                * Then add arr[i] into the leftEvenSum/leftOddSum
                  for next iterations.

        Time  : O(n)
        Space : O(1)  (just a handful of counters)
        """
        n = len(arr)
        if n == 0:
            return 0

        # 1) Compute initial right-side sums (even and odd indices)
        right_even_sum = 0
        right_odd_sum = 0
        for i, value in enumerate(arr):
            if i % 2 == 0:
                right_even_sum += value
            else:
                right_odd_sum += value

        # 2) Left-side sums start at zero
        left_even_sum = 0
        left_odd_sum = 0

        valid_indices = 0

        # 3) Iterate treating each index as the removed one
        for i, value in enumerate(arr):
            # Remove current value from the right side
            if i % 2 == 0:
                right_even_sum -= value
            else:
                right_odd_sum -= value

            # After removal, right side shifts:
            # old-right-odd -> new-even, old-right-even -> new-odd
            new_even_sum = left_even_sum + right_odd_sum
            new_odd_sum = left_odd_sum + right_even_sum

            if new_even_sum == new_odd_sum:
                valid_indices += 1

            # Add current element to left side for next positions
            if i % 2 == 0:
                left_even_sum += value
            else:
                left_odd_sum += value

        return valid_indices