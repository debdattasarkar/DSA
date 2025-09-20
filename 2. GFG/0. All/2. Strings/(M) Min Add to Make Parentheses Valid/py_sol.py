class Solution:
    def minParentheses(self, s):
        """
        Single pass counter.
        Time  : O(n)  (one scan)
        Space : O(1)  (two integers)
        """
        balance = 0  # unmatched '('
        need = 0     # number of '(' we must insert for unmatched ')'
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    need += 1
        # 'need' covers extra ')', 'balance' covers extra '('
        return need + balance