import heapq

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]

        ans = -10**18
        heap = []  # (P[i], i)

        for j in range(a, n+1):
            # Add freshly eligible index i = j - a
            i_add = j - a
            heapq.heappush(heap, (P[i_add], i_add))

            # Expire indices with i < j - b
            lower = j - b
            if lower < 0:
                lower = 0
            while heap and heap[0][1] < lower:
                heapq.heappop(heap)

            # Current min prefix in window -> heap[0]
            ans = max(ans, P[j] - heap[0][0])
        return ans