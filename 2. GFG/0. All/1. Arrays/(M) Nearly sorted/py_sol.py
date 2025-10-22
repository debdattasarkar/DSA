import heapq

class Solution:
    def nearlySorted(self, arr, k):  
        """
        Min-heap of size k+1
        Time  : O(n log k)   (each of n pushes/pops is log(k+1))
        Space : O(k)         (heap only)
        """
        n = len(arr)
        if n <= 1 or k <= 0:
            return arr  # already sorted or trivial

        # 1) Build heap from first k+1 elements
        heap = arr[:k+1]
        heapq.heapify(heap)        # O(k)

        write = 0                  # next position to place smallest element

        # 2) For remaining elements, push new, pop min to 'write'
        for read in range(k+1, n):
            smallest = heapq.heapreplace(heap, arr[read])  # pop min + push arr[read]
            arr[write] = smallest
            write += 1

        # 3) Drain the heap
        while heap:
            arr[write] = heapq.heappop(heap)
            write += 1

        return arr