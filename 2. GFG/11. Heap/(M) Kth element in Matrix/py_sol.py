import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        n = len(matrix)
        min_heap = []

        # Push the first element of each row into the heap
        for i in range(min(k, n)):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, col)

        # Pop from heap k times
        count = 0
        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            count += 1
            if count == k:
                return val
            # If there's another element in the same row, push it
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))