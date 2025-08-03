class Solution:
    def countConsec(self, n: int) -> int:
        # code here 
        
        # Total binary strings of length n
        total = 2 ** n
        
        # dp[i] stores number of strings of length i without consecutive 1's
        prev2, prev1 = 1, 2  # dp[0], dp[1]
        
        if n == 0:
            return 0
        if n == 1:
            return 0  # Only "11" has consecutive 1s for n >= 2
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        
        # Strings with at least one pair of consecutive 1's
        with_consec = total - prev1

        return with_consec