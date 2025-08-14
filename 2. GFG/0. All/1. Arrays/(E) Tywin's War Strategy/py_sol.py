class Solution:
    def minSoldiers(self, arr, k):
        # code here
        """
        Returns the minimal total soldiers to add so that at least ceil(n/2)
        troops have sizes divisible by k.

        Time:  O(n log n)  -- sorting the costs
        Space: O(n)        -- list of costs (can be optimized to O(1) extra if reused)
        """
        n = len(arr)
        if n == 0:
            return 0
        if k == 1:
            # Every number is divisible by 1; already all lucky
            return 0

        # Compute extra soldiers needed for each troop to reach next multiple of k
        costs = []
        already = 0
        for x in arr:
            r = x % k
            c = (k - r) % k  # 0 if already multiple; else gap to next multiple
            if c == 0:
                already += 1
            else:
                costs.append(c)

        target = (n + 1) // 2  # ceil(n/2)
        need = max(0, target - already)
        if need == 0:
            return 0

        costs.sort()
        return sum(costs[:need])