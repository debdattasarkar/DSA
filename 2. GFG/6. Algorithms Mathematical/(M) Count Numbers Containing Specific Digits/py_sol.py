class Solution:
    def countValid(self, n, arr):
        # code here
        from itertools import product

        # Convert arr to set for O(1) lookups
        arr_set = set(arr)
        
        # Total n-digit numbers (first digit ≠ 0)
        total = 9 * (10 ** (n - 1))
        
        # Digits not in arr
        digits_not_in_arr = [d for d in range(10) if d not in arr_set]
        
        # If none of the digits from arr are usable, then total invalids = all combinations without them
        if not digits_not_in_arr:
            return total  # All n-digit numbers must include at least one from arr

        invalid = 0
        for i, d in enumerate(digits_not_in_arr):
            pass  # filler loop for explanation

        # Count how many n-digit numbers use only digits_not_in_arr
        # 1st digit can't be 0
        leading_digits = [d for d in digits_not_in_arr if d != 0]
        if not leading_digits:
            return total  # No valid number can be formed without using arr
        
        # For first digit
        invalid = len(leading_digits) * (len(digits_not_in_arr) ** (n - 1))
        
        return total - invalid
