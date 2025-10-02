class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		"""
        Idea: sort value-index pairs to know each element's target position.
        Walk permutation cycles; sum (cycle_len - 1).

        Time:  O(n log n) for the sort, O(n) to walk cycles
        Space: O(n) for pairs + visited
        """
        n = len(arr)
        # Pair each value with its original index, then sort by value
        with_idx = [(val, i) for i, val in enumerate(arr)]      # O(n)
        with_idx.sort(key=lambda x: x[0])                        # O(n log n)

        visited = [False] * n                                    # O(n) space
        swaps = 0

        for i in range(n):                                       # O(n)
            # If already visited or already in correct place, skip
            if visited[i] or with_idx[i][1] == i:
                continue

            # Follow the cycle starting at i
            cycle_len = 0
            j = i
            while not visited[j]:                                # each index visited once overall
                visited[j] = True
                # Jump to the index where the current element originally came from
                j = with_idx[j][1]
                cycle_len += 1

            if cycle_len > 0:
                swaps += cycle_len - 1                           # L-1 swaps per cycle

        return swaps