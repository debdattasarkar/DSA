class Solution:
    def getCount(self, n, d):
        # Compute digit sum in O(number_of_digits)
        # Time: O(log10(x)), Space: O(1)
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        # Check function: is x valid?
        # Time: O(digits), Space: O(1)
        def is_valid(x):
            return x - digit_sum(x) >= d

        # Binary search for smallest x in [1..n] that is valid
        # Time: O(log n) checks, each check O(digits)
        left, right = 1, n
        first_ok = -1

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                first_ok = mid       # mid works, try to find smaller
                right = mid - 1
            else:
                left = mid + 1       # mid doesn't work, go bigger

        # If none found, answer is 0
        if first_ok == -1:
            return 0

        # All numbers from first_ok to n are valid
        return n - first_ok + 1