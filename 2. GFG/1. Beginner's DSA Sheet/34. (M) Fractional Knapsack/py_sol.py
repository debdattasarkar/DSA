class Solution:
    # Optimized Greedy (sort by value/weight)
    def fractionalKnapsack(self, val, wt, capacity):
        """
        Time:  O(n log n) due to sorting
        Space: O(n) to store (ratio, value, weight)
        """
        items = [(val[i]/wt[i], val[i], wt[i]) for i in range(len(val))]
        items.sort(key=lambda x: x[0], reverse=True)  # by ratio desc

        total, remaining = 0.0, capacity
        for ratio, v, w in items:
            if remaining == 0:
                break
            if w <= remaining:         # take whole item
                total += v
                remaining -= w
            else:                      # take fractional part and stop
                total += v * (remaining / w)
                remaining = 0
                break

        return round(total, 6)

    # Brute/Easy (no sort; repeatedly pick best ratio by linear scan)
    def fractionalKnapsack_brutish(self, val, wt, capacity):
        """
        Time:  O(k*n) (worst-case O(n^2)), Space: O(n)
        Repeatedly find the unused max-ratio item by scanning.
        """
        n, used = len(val), [False]*len(val)
        total, remaining = 0.0, capacity

        while remaining > 0:
            best, idx = -1.0, -1
            for i in range(n):
                if not used[i]:
                    r = val[i]/wt[i]
                    if r > best:
                        best, idx = r, i
            if idx == -1:  # nothing left
                break

            used[idx] = True
            if wt[idx] <= remaining:
                total += val[idx]
                remaining -= wt[idx]
            else:
                total += val[idx] * (remaining / wt[idx])
                remaining = 0
                break

        return round(total, 6)

    # Heap-based Greedy (priority queue by ratio)
    def fractionalKnapsack_heap(self, val, wt, capacity):
        """
        Time:  O(n log n), Space: O(n)
        Uses a max-heap (implemented as negatives in Python).
        """
        import heapq
        heap = [(-(v/w), v, w) for v, w in zip(val, wt)]
        heapq.heapify(heap)

        total, remaining = 0.0, capacity
        while heap and remaining > 0:
            _, v, w = heapq.heappop(heap)
            if w <= remaining:
                total += v
                remaining -= w
            else:
                total += v * (remaining / w)
                remaining = 0
        return round(total, 6)
