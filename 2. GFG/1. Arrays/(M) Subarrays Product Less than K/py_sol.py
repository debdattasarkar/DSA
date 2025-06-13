#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        if k <= 1:
            return 0
        
        prod = 1
        result = 0
        start = 0

        for end in range(n):
            prod *= a[end]
            while prod >= k:
                prod //= a[start]
                start += 1
            result += end - start + 1
        
        return result