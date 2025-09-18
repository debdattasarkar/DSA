class Solution:
    def countAndSay(self, n):
        """
        Generate the nth term by iterating from the seed "1".

        Let L_k be the length of the k-th term; L_k grows ~ O(1.3^k).
        Time  : proportional to total characters processed
                = sum_{i=1..n} L_i  (≈ exponential in n; n ≤ 30 is fine)
        Space : O(L_n) for the final string / current builder
        """
        term = "1"                           # row 1
        for _ in range(1, n):                # build n-1 times
            i, m = 0, len(term)
            out_parts = []                   # use list builder (amortized O(1) append)
            while i < m:
                j = i
                # count run of the same digit
                while j < m and term[j] == term[i]:
                    j += 1
                count = j - i
                out_parts.append(str(count)) # append "count" then the digit
                out_parts.append(term[i])
                i = j
            term = "".join(out_parts)        # O(length of next term)
        return term