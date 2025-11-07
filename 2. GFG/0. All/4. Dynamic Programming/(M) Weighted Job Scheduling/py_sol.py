from bisect import bisect_right

class Solution:
    def maxProfit(self, jobs):
        """
        Iterative DP on end-sorted jobs.
        dp[i] = max profit using the first i jobs (i = 0..n)
        Transition with job k = i-1:
            j = count of jobs that finish ≤ start[k] among first (i-1)
            dp[i] = max(dp[i-1], profit[k] + dp[j])
        Time:  O(n log n)
        Space: O(n)
        """
        jobs.sort(key=lambda x: x[1])            # 1) sort by end
        n = len(jobs)
        ends = [e for _, e, _ in jobs]           # for binary search on predecessors
        dp = [0] * (n + 1)                       # dp[0] = 0 (no job)

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]                # current job (0-based)
            # among the first (i-1) jobs (ends[:i-1]), count those with end ≤ s
            j = bisect_right(ends, s, 0, i - 1)  # predecessor prefix length
            take = p + dp[j]                     # take job → add best up to j jobs
            skip = dp[i - 1]                     # skip job
            dp[i] = take if take > skip else skip

        return dp[n]
