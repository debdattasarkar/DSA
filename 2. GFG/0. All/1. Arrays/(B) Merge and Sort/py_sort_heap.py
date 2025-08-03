#User function Template for python3
import heapq

class Solution:
    def mergeNsort(self, arr, brr):
        # Write your code here
        # Step 1: Combine both arrays
        combined = arr + brr
        
        # Step 2: Remove duplicates using set
        unique = set(combined)
        
        # Step 3: Convert set to a list and heapify it
        heap = list(unique)
        heapq.heapify(heap)  # O(n)
        
        # Step 4: Pop elements in sorted order
        result = []
        while heap:
            result.append(heapq.heappop(heap))  # O(log n) per pop
        
        return result