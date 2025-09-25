class Solution:
    def palindromicSubstr(self, s):
        n = len(s)
        seen = set()
        
        # Expand from a given center (l,r) and add palindromes
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                # s[l:r+1] is a palindrome; store distinct
                seen.add(s[l:r+1])
                l -= 1
                r += 1
        
        # Consider all odd and even centers
        for i in range(n):
            expand(i, i)       # odd-length palindromes centered at i
            expand(i, i + 1)   # even-length palindromes centered between i and i+1
        
        return sorted(seen)