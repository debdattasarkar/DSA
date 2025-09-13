class Solution:    
    def minPlatform(self, arr, dep):
        """
        Two-pointer sweep after sorting arrival and departure times.

        Time:  O(n log n) for sorting
        Space: O(1) extra (if we can sort in place)  [ignoring sort's stack]
        """
        n = len(arr)
        if n == 0:
            return 0

        arr.sort()  # O(n log n)
        dep.sort()  # O(n log n)

        i = j = 0          # i -> next arrival, j -> next departure
        curr = maxp = 0

        # Traverse both lists
        while i < n and j < n:             # O(n)
            if arr[i] <= dep[j]:
                # Arrival needs a platform (<= handles same-time overlap)
                curr += 1
                maxp = max(maxp, curr)
                i += 1
            else:
                # Earliest departure frees a platform
                curr -= 1
                j += 1

        return maxp