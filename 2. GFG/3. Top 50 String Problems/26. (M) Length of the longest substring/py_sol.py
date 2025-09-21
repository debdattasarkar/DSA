#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):
        # Sliding window with last-seen indices
        # Time  : O(n) (each index advances at most once)
        # Space : O(min(n, alphabet)) for the map
        
        last = {}            # char -> last index seen
        l = 0                # left boundary of current window
        best = 0
        
        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                # ch repeated within current window [l..r-1]:
                # move l just after last occurrence
                l = last[ch] + 1
            # update best with current window length
            best = max(best, r - l + 1)
            # remember where we saw ch
            last[ch] = r
        
        return best