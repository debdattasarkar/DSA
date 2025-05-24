class Solution:
    def sumSubstrings(self,s):
        # code here
        n = len(s)
        total = int(s[0])
        prev = total

        for i in range(1, n):
            num = int(s[i])
            curr = prev * 10 + num * (i + 1)
            total += curr
            prev = curr
        
        return total