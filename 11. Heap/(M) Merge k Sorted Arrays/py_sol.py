class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        # Min heap to keep track of the minimum element
        min_heap = []
        
        # Step 1: Push the first element of each array into the heap
        for i in range(K):
            heapq.heappush(min_heap, (arr[i][0], i, 0))  # (value, row, col)
        
        result = []
        
        # Step 2: Extract min and insert next element from the same row
        while min_heap:
            val, row, col = heapq.heappop(min_heap)
            result.append(val)
            if col + 1 < K:
                heapq.heappush(min_heap, (arr[row][col + 1], row, col + 1))
        
        return result