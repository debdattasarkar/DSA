import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        #code here
        # Step 1: Count frequency of each character
        freq = Counter(s)
        
        # Step 2: Use a max-heap (invert to simulate max-heap)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)

        # Step 3: Perform k removals
        while k > 0 and max_heap:
            top = heapq.heappop(max_heap)
            top += 1  # Since negative, incrementing means reducing abs value
            if top < 0:
                heapq.heappush(max_heap, top)
            k -= 1

        # Step 4: Calculate sum of squares of remaining frequencies
        return sum(x * x for x in max_heap)  # still negative, so square cancels