class Solution:
    def maxMinDiff(self, arr, k):
        # code here
        """
        Sort + binary search the answer.
        Time:  O(n log n) for sort + O(n log R) for search (R = max-min)  ~ O(n log n)
        Space: O(1) extra (in-place sort aside)
        """
        n = len(arr)
        if k <= 1 or n <= 1:
            return 0

        arr.sort()  # O(n log n)

        # Greedy feasibility: can we pick k numbers with pairwise gap >= D?
        def can_place(D: int) -> bool:
            count = 1               # pick the first element
            last = arr[0]
            for x in arr[1:]:
                if x - last >= D:   # place next as soon as gap allows
                    count += 1
                    last = x
                    if count == k:  # early exit
                        return True
            return False

        lo, hi = 0, arr[-1] - arr[0]
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid          # mid is feasible; try for a larger gap
                lo = mid + 1
            else:
                hi = mid - 1       # mid is too large; reduce
        return ans

