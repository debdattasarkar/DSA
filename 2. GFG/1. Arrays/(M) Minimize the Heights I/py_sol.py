#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        arr.sort()  # Sort the array

        ans = arr[-1] - arr[0]  # Initial difference

        for i in range(n - 1):
            high = max(arr[-1] - k, arr[i] + k)
            low = min(arr[0] + k, arr[i + 1] - k)

            if low < 0:
                continue  # skip if height goes negative

            ans = min(ans, high - low)

        return ans