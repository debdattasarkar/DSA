import heapq
class Solution:
    def kClosest(self, points, k):
        """
        Keep k closest points in a max-heap (store negative distances to use Python min-heap).
        Time  : O(n log k)
        Space : O(k)
        """
        # Max-heap via negatives: ( -dist2, x, y )
        heap = []
        for x, y in points:
            dist2 = x*x + y*y  # squared distance is enough
            if len(heap) < k:
                heapq.heappush(heap, (-dist2, x, y))  # push until size k
            else:
                # If current point is closer than the farthest in heap → replace
                if -dist2 > heap[0][0]:              # compare to current max (-dist2 larger => closer)
                    heapq.heapreplace(heap, (-dist2, x, y))
                # else: ignore; it's farther than the current top-k
        # Extract the k points from heap (any order is fine)
        return [[x, y] for _, x, y in heap]