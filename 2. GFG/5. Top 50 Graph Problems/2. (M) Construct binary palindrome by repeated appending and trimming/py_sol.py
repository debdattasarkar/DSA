
class Solution:
    def binaryPalindrome(self, n : int, k : int) -> str:
        # code here
        # We want a k-periodic palindrome S of length n, with as many zeros as possible,
        # and the k-length block starts with '1' (i.e., residue 0 is '1').
        #
        # Let p = (n - 1) % k. By palindromic constraints, residue 0 is paired with residue p,
        # so both must be equal; since the block must start with '1', we set residues {0, p} to '1'
        # and all other residues to '0' to maximize zeros.
        #
        # Thus, for every position i, S[i] = '1' iff i % k in {0, p}; otherwise '0'.

        if n <= 0 or k <= 0:
            return "-1"

        p = (n - 1) % k

        # Build answer directly in O(n), O(1) extra space (aside from output).
        res_chars = []
        for i in range(n):
            r = i % k
            res_chars.append('1' if r == 0 or r == p else '0')

        return ''.join(res_chars)
        
