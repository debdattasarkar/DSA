#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        diff = arr[-1] - arr[0]

        for i in range(n - 1):
            min_elem = min(arr[0] + k, arr[i + 1] - k)
            max_elem = max(arr[i] + k, arr[-1] - k)
            if min_elem < 0:
                continue
            diff = min(diff, max_elem - min_elem)
        
        return diff