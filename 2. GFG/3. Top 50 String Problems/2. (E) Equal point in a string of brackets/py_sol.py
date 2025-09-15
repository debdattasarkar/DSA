#User function Template for python3

class Solution:
    def findIndex(self,s):
        """
        Idea:
        - Let opens = count of '(' seen in prefix [0:i)
        - Let closesRight = count of ')' in suffix [i:n)
        - Initially, opens = 0 and closesRight = total number of ')'
        - At each boundary i, check opens == closesRight -> equal point
        - Then consume s[i], updating either opens (for '(') or closesRight (for ')')
        Time:  O(n)
        Space: O(1)
        """
        n = len(s)
        closesRight = s.count(')')  # total closers in the entire string
        opens = 0                   # opens in the prefix
        
        # Check all boundaries i = 0..n-1 before consuming s[i]
        for i, ch in enumerate(s):
            if opens == closesRight:   # boundary i is equal point
                return i
            if ch == '(':
                opens += 1             # we add one '(' to the left
            else:
                closesRight -= 1       # we remove one ')' from the right
        
        # Check last boundary i = n
        return n if opens == closesRight else -1