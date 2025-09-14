class Solution:
    def equalPartition(self, arr):
        """
        1-D subset-sum DP to reach total/2.
        Time:  O(n * target)   where target = sum(arr)//2
        Space: O(target)
        """
        total = sum(arr)
        # odd total can't be split equally
        if total & 1:
            return False
        target = total // 2

        # dp[t] == True if some subset makes sum t
        dp = [False] * (target + 1)
        dp[0] = True  # empty subset makes 0

        for x in arr:
            # iterate backwards so each number is used at most once
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            if dp[target]:               # early exit optimization
                return True

        return dp[target]