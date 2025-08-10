class Solution:
    def countPS(self, s):
        # code here
        n = len(s)
        if n < 2:
            return 0
        
        def expand(l, r):
            # Expands while s[l..r] is a palindrome
            # Counts only substrings with length >= 2
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    cnt += 1
                l -= 1
                r += 1
            return cnt
        
        total = 0
        for i in range(n):
            # Odd-length palindromes centered at i
            total += expand(i, i)
            # Even-length palindromes centered between i and i+1
            total += expand(i, i + 1)
        return total