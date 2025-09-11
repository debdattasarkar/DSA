from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n = len(arr)
        result = []
        dq = deque()  # Stores indices of elements

        for i in range(n):
            # Remove elements out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements (they are useless)
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Append the max of current window
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result