class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Everyone gets at least 1 candy
        candies = [1] * n  # Space: O(n)

        # 1) Left to Right: if rating increases, candies must increase
        # Time: O(n)
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 2) Right to Left: if rating increases from right, fix using max
        # Time: O(n)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Sum candies
        # Time: O(n)
        return sum(candies)