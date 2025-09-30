class Solution:
    def maxHeight(self,height, width, length):
        """
        Build all 3 rotations per box; sort by base area desc; LIS-style DP.
        Time:  O((3n)^2)  ≤ O(9n^2)  (n ≤ 100 on GFG -> fast)
        Space: O(3n)
        """
        n = len(height)
        # 1) Generate rotations as (base_longer, base_shorter, H)
        rots = []
        for h, w, l in zip(height, width, length):
            # rotation 1: height=h, base=(w,l)
            bL, bS = (w, l) if w >= l else (l, w)
            rots.append((bL, bS, h))
            # rotation 2: height=w, base=(h,l)
            bL, bS = (h, l) if h >= l else (l, h)
            rots.append((bL, bS, w))
            # rotation 3: height=l, base=(h,w)
            bL, bS = (h, w) if h >= w else (w, h)
            rots.append((bL, bS, l))

        # 2) Sort by base area descending; tie-break by bL, then bS (desc) for stability
        rots.sort(key=lambda x: (x[0] * x[1], x[0], x[1]), reverse=True)

        m = len(rots)
        # dp[i] = best height ending at i (i on top)
        dp = [h for (_, _, h) in rots]  # base case: stack of only this rotation

        # 3) Standard 2D LIS with strict inequality on both base sides
        for i in range(m):
            for j in range(i):  # j below i
                if rots[j][0] > rots[i][0] and rots[j][1] > rots[i][1]:
                    dp[i] = max(dp[i], dp[j] + rots[i][2])

        return max(dp) if dp else 0