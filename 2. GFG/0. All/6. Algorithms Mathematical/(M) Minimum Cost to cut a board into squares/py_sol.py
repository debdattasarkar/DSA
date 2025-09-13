class Solution:
    def minCost(self, n, m, x, y):
        """
        Greedy: sort both cost arrays descending and always pick
        the next larger cut cost first.
        
        Time:  O((n+m) log(n+m)) due to sorting
        Space: O(1) extra (sorting in-place is fine; result uses O(1))
        """
        # Sort descending so we consume largest costs first
        x.sort(reverse=True)  # vertical cuts (m-1)
        y.sort(reverse=True)  # horizontal cuts (n-1)

        i = j = 0                     # pointers in x and y
        v_segments = 1                # number of vertical segments (columns)
        h_segments = 1                # number of horizontal segments (rows)
        total = 0

        # While both lists still have cuts left, pick the costlier next cut
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                # Take vertical cut: cost multiplied by current #horizontal segments
                total += x[i] * h_segments
                v_segments += 1
                i += 1
            else:
                # Take horizontal cut: cost multiplied by current #vertical segments
                total += y[j] * v_segments
                h_segments += 1
                j += 1

        # Any remaining vertical cuts
        while i < len(x):
            total += x[i] * h_segments
            v_segments += 1
            i += 1

        # Any remaining horizontal cuts
        while j < len(y):
            total += y[j] * v_segments
            h_segments += 1
            j += 1

        return total