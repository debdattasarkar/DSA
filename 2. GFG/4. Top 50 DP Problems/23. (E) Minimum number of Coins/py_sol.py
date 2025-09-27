class Solution:
    def findMin(self, n):
        # Handle n = 0 gracefully (though constraints say n >= 1)
        if n <= 0:
            return 0
        
        # Count 10-rupee coins
        c10 = n // 10             # O(1)
        n  %= 10                  # O(1)
        
        # Count 5-rupee coins from remainder
        c5  = n // 5              # O(1)
        n  %= 5                   # O(1)
        
        # Count 2-rupee coins from remainder
        c2  = n // 2              # O(1)
        n  %= 2                   # O(1)
        
        # Remaining are 1-rupee coins
        c1  = n                   # O(1)
        
        # Total coins is sum of counts
        return c10 + c5 + c2 + c1