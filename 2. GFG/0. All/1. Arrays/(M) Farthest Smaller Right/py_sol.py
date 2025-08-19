class Solution:
    def farMin(self, arr):
        # Code Here
        n = len(arr)
        if n == 0:
            return []
        
        # 1) Build suffix minima: smin[i] = min(arr[i..n-1])
        #    Time: O(n), Space: O(n)
        smin = [0] * n
        smin[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            smin[i] = arr[i] if arr[i] < smin[i + 1] else smin[i + 1]
        
        # 2) For each i, binary-search largest pos in (i..n-1] with smin[pos] < arr[i]
        #    Time: O(n log n)
        ans = [-1] * n
        for i in range(n - 1):                 # last index remains -1
            lo, hi = i + 1, n - 1
            far = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if smin[mid] < arr[i]:
                    far = mid                  # candidate farthest so far
                    lo = mid + 1               # try to go even farther right
                else:
                    hi = mid - 1
            ans[i] = far
        
        return ans