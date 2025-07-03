import timeit

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            """
            Compute the next number by summing squares of digits.
            Time Complexity: O(log n) - since number of digits is log₁₀(n)
            Space Complexity: O(1)
            """
            total = 0
            while num > 0:
                digit = num % 10          # extract last digit
                total += digit * digit    # square it and add
                num //= 10                # remove last digit
            return total

        # Use Floyd’s Cycle Detection
        slow = n
        fast = get_next(n)  # fast pointer moves ahead one step

        # Continue until we find 1 (happy number) or a cycle
        while fast != 1 and slow != fast:
            slow = get_next(slow)             # move one step
            fast = get_next(get_next(fast))   # move two steps

        return fast == 1

# ------------------ Sample Input & Output ------------------ #

sol = Solution()

# Example 1
n1 = 19
print(f"Input: {n1}, Output: {sol.isHappy(n1)}")  # True

# Example 2
n2 = 2
print(f"Input: {n2}, Output: {sol.isHappy(n2)}")  # False

# ------------------ Timing with timeit ------------------ #

def benchmark():
    sol = Solution()
    sol.isHappy(19)
    sol.isHappy(2)
    sol.isHappy(7)
    sol.isHappy(1111111)

# Measure time over 10000 runs
execution_time = timeit.timeit(benchmark, number=10000)
print(f"Execution time over 10,000 runs: {execution_time:.5f} seconds")
