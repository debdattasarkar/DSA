#User function Template for python3

class Solution:
    def partitionArray(self,N,K,M,arr):
        """
        Determine if arr can be partitioned into groups of size >= K
        where max-min within each group <= M.

        Steps:
          1. Sort -> groups become contiguous.
          2. dp[i] = feasibility for first i elements (0..i-1)
          3. For group ending at i-1, valid start j in [L..i-K],
             where L is the smallest index with a[i-1] - a[L] <= M.
          4. Use a prefix sum of booleans to check "any dp[j] is True in [L..i-K]" in O(1).

        Time:  O(N log N) for sort + O(N) scan  => overall O(N log N)
        Space: O(N) for dp + prefix
        """
        a = sorted(arr)
        n = N

        # dp[i] -> can we partition first i elements?  dp[0] = True (empty prefix)
        dp = [False] * (n + 1)
        dp[0] = True

        # pref[i] = number of True dp[0..i]
        pref = [0] * (n + 1)
        pref[0] = 1  # dp[0] is True

        l = 0  # leftmost index such that a[i-1] - a[l] <= M

        for i in range(1, n + 1):
            # Move l forward until the block [l..i-1] satisfies (max-min) <= M
            while l < i and a[i - 1] - a[l] > M:
                l += 1

            # The last group must have size at least K:
            # eligible start indices j ∈ [l .. i-K]
            left = l
            right = i - K

            ok = False
            if right >= left:
                # Does there exist j in [left..right] with dp[j] == True?
                # Use prefix sums of dp-True counts:
                # countTrue = pref[right] - pref[left - 1]
                countTrue = pref[right] - (pref[left - 1] if left - 1 >= 0 else 0)
                ok = (countTrue > 0)

            dp[i] = ok
            pref[i] = pref[i - 1] + (1 if dp[i] else 0)

        return dp[n]