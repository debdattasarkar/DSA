class Solution:
    def findTwoElement(self, arr):
        """
        Return [repeating, missing]
        Math approach using sums and sum of squares.
        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)

        # Expected sums for 1..n
        S = n * (n + 1) // 2
        SS = n * (n + 1) * (2 * n + 1) // 6

        # Actual sums from array
        s = 0
        ss = 0
        for x in arr:
            s += x          # O(n)
            ss += x * x

        diff = s - S        # = R - M
        sqdiff = ss - SS    # = (R - M)(R + M)

        # Avoid division by zero theoretically; per problem guarantees diff != 0
        sum_rm = sqdiff // diff   # = R + M

        R = (sum_rm + diff) // 2
        M = sum_rm - R

        return [R, M]