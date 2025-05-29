import heapq

class Solution:
    def getMedian(self, arr):
        low = []  # max-heap (invert values)
        high = []  # min-heap
        result = []

        for num in arr:
            # Insert into max heap (as negative number)
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
            else:
                heapq.heappush(high, num)

            # Rebalance heaps
            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            elif len(high) > len(low):
                heapq.heappush(low, -heapq.heappop(high))

            # Get median
            if len(low) == len(high):
                median = (-low[0] + high[0]) / 2.0
            else:
                median = float(-low[0])
            result.append(median)

        return result