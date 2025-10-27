class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        """
        Optimized: best-first search using a min-heap.
        Time:  O(k log k)   | Space: O(k)
        Assumes arr1 and arr2 are sorted ascending.
        Returns a list of k pairs [arr1[i], arr2[j]] with smallest sums.
        """
        import heapq

        n, m = len(arr1), len(arr2)
        if n == 0 or m == 0 or k <= 0:
            return []

        # Each heap item: (sum, i, j)
        min_heap = []
        result_pairs = []

        # Seed with the first pair (0,0)
        heapq.heappush(min_heap, (arr1[0] + arr2[0], 0, 0))

        # To avoid pushing the same (i, j) more than once, we track visited states.
        # (For this specific pattern of pushes, visited isn’t strictly necessary,
        #  but we include it to be robust and interview-friendly.)
        visited = set()
        visited.add((0, 0))

        while min_heap and len(result_pairs) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result_pairs.append([arr1[i], arr2[j]])

            # Candidate 1: move right in arr2 (same i, j+1)
            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (arr1[i] + arr2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            # Candidate 2: move down in arr1 (i+1, same j) — only when j == 0
            # This ensures each row i is introduced exactly once (at column 0).
            if j == 0 and i + 1 < n and (i + 1, 0) not in visited:
                heapq.heappush(min_heap, (arr1[i + 1] + arr2[0], i + 1, 0))
                visited.add((i + 1, 0))

        return result_pairs