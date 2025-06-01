#User function Template for python3
import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        minHeap = []
        result = []

        for num in arr:
            heapq.heappush(minHeap, num)  # Add number to heap

            # Maintain heap size at most k
            if len(minHeap) > k:
                heapq.heappop(minHeap)

            # If heap has fewer than k elements, k-th largest doesn't exist yet
            if len(minHeap) < k:
                result.append(-1)
            else:
                result.append(minHeap[0])  # Top of min-heap is k-th largest

        return result