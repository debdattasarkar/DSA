class Solution:
    def sumOfModes(self, arr, k):
        """
        Optimized: Sliding window + max-heap with lazy deletion.
        Heap stores tuples (-freq, value); smallest tuple at top is our mode
        because:
          - higher freq -> smaller -freq
          - tie on freq: smaller value wins automatically
        Time:  O(n log k)  (push/pop per slide)
        Space: O(k)        (freq map + heap of window-sized items)
        """
        n = len(arr)
        if k == 0 or n == 0:
            return 0
        if k == 1:
            # Each window has 1 element -> mode is that element
            return sum(arr)

        freq = defaultdict(int)       # value -> current frequency in window
        heap = []                     # entries are (-freq, value)

        # --- build the first window: O(k log k) for heap pushes, O(k) for freq
        for x in arr[:k]:
            freq[x] += 1
        for v, f in freq.items():
            heapq.heappush(heap, (-f, v))

        def clean_top():
            """Pop stale heap entries until top matches current freq.
               Amortized O(log k) across the run."""
            while heap:
                negf, val = heap[0]
                f = -negf
                if freq.get(val, 0) != f:   # stale
                    heapq.heappop(heap)
                else:
                    break

        clean_top()
        total = 0
        total += heap[0][1]  # mode value of first window

        # --- slide the window across the array: O((n-k) log k)
        for r in range(k, n):
            add_val = arr[r]
            rem_val = arr[r - k]

            # 1) add entering element
            freq[add_val] += 1
            heapq.heappush(heap, (-freq[add_val], add_val))

            # 2) remove leaving element
            freq[rem_val] -= 1
            if freq[rem_val] == 0:
                del freq[rem_val]
            else:
                heapq.heappush(heap, (-freq[rem_val], rem_val))

            # 3) query mode = valid top of heap
            clean_top()
            total += heap[0][1]

        return total
