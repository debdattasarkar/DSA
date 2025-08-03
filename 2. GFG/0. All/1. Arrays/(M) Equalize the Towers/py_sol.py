class Solution:
    def minCost(self, heights, cost):
        # code here
        def compute_total(h):
            return sum(abs(h - heights[i]) * cost[i] for i in range(len(heights)))

        left, right = min(heights), max(heights)
        ans = compute_total(heights[0])

        while left < right:
            mid = (left + right) // 2
            cost1 = compute_total(mid)
            cost2 = compute_total(mid + 1)

            ans = min(cost1, cost2)

            if cost1 < cost2:
                right = mid
            else:
                left = mid + 1

        return ans