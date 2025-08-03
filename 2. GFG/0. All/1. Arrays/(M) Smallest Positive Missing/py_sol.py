class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)

        # Step 1: Replace non-positive and >n numbers with a placeholder
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1  # ignore these numbers

        # Step 2: Mark the presence
        for i in range(n):
            num = abs(arr[i])
            if 1 <= num <= n:
                if arr[num - 1] > 0:
                    arr[num - 1] = -arr[num - 1]

        # Step 3: First missing index
        for i in range(n):
            if arr[i] > 0:
                return i + 1  # index+1 is missing

        return n + 1  # if all 1..n are present