class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # ---------- Helper arrays ----------
        prev_greater = [-1] * n        # previous index with value > arr[i]
        next_greater_eq = [n] * n      # next index with value >= arr[i]

        prev_smaller = [-1] * n        # previous index with value < arr[i]
        next_smaller_eq = [n] * n      # next index with value <= arr[i]

        # ---------- 1) prev_greater (strict >) ----------
        # Maintain a decreasing stack (values strictly greater remain)
        stack = []
        for i in range(n):
            # Pop while top <= current, so remaining top (if any) is strictly greater
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        # ---------- 2) next_greater_eq (>=) ----------
        # Scan from right. Pop while top < current, so remaining top (if any) is >= current
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_greater_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # ---------- 3) prev_smaller (strict <) ----------
        # Maintain an increasing stack (values strictly smaller remain)
        stack = []
        for i in range(n):
            # Pop while top >= current, so remaining top (if any) is strictly smaller
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # ---------- 4) next_smaller_eq (<=) ----------
        # Scan from right. Pop while top > current, so remaining top (if any) is <= current
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # ---------- Compute sums ----------
        sum_of_max = 0
        sum_of_min = 0

        for i in range(n):
            # count subarrays where arr[i] is max
            left_max_choices = i - prev_greater[i]
            right_max_choices = next_greater_eq[i] - i
            sum_of_max += arr[i] * left_max_choices * right_max_choices

            # count subarrays where arr[i] is min
            left_min_choices = i - prev_smaller[i]
            right_min_choices = next_smaller_eq[i] - i
            sum_of_min += arr[i] * left_min_choices * right_min_choices

        return sum_of_max - sum_of_min