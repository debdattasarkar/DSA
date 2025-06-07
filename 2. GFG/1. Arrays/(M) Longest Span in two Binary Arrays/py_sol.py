class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]
        
        prefix_sum = 0
        max_len = 0
        mp = {}  # map: prefix_sum -> first index

        for i in range(n):
            prefix_sum += diff[i]
            
            if prefix_sum == 0:
                max_len = i + 1
            elif prefix_sum in mp:
                max_len = max(max_len, i - mp[prefix_sum])
            else:
                mp[prefix_sum] = i
        
        return max_len