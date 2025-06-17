class Solution:
    def minimumCoins(self, arr, k):
        # code here
         # Step 1: Sort the coin values
        arr.sort()

        # Step 2: Prepare prefix sum array
        n = len(arr)
        pre = [0]
        for x in arr:
            pre.append(pre[-1] + x)

        # Step 3: Initialize result with the sum of all coins
        res = pre[-1]
        j = 0

        # Step 4: Try each coin as base value to compare others with
        for i in range(n):
            # Move j forward until arr[j] > arr[i] + k
            while j < n and arr[j] <= arr[i] + k:
                j += 1

            # Calculate cost to reduce all coins greater than arr[i]+k
            if j < n:
                large = pre[-1] - pre[j] - (n - j) * (arr[i] + k)
            else:
                large = 0

            # Total cost = sum of smaller/equal values + cost to reduce big ones
            res = min(res, pre[i] + large)

        return res