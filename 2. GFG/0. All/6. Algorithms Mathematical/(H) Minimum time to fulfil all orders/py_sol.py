class Solution:
    def minTime(self, ranks, n):
        # Edge case
        if n == 0:
            return 0

        # ---------- Feasibility check ----------
        # Time: O(m * donuts_per_chef) but donuts_per_chef <= n (n<=1000)
        # Space: O(1)
        def can_make_in_time(time_limit):
            total_donuts = 0

            for rank in ranks:
                time_spent = 0
                donut_number = 1

                # Each chef makes donuts until time exceeds limit
                while True:
                    next_time = rank * donut_number
                    if time_spent + next_time > time_limit:
                        break
                    time_spent += next_time
                    total_donuts += 1
                    donut_number += 1

                    if total_donuts >= n:  # early stop
                        return True

            return total_donuts >= n

        # ---------- Binary search bounds ----------
        # Low: 0
        low = 0

        # High: fastest chef makes all n donuts
        # Time = r_min * (1+2+...+n) = r_min * n*(n+1)/2
        fastest_rank = min(ranks)
        high = fastest_rank * n * (n + 1) // 2

        # ---------- Binary Search on answer ----------
        # Time: O(log high)
        while low < high:
            mid = (low + high) // 2
            if can_make_in_time(mid):
                high = mid
            else:
                low = mid + 1

        return low