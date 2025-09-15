#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        """
        Repeat A just enough to cover B, then one more time for overlap.
        Check substring membership using Python's 'in' (efficient under the hood).

        Let n = len(A), m = len(B), k = ceil(m / n).
        Time : O(n * k + m) overall for building + membership (amortized ~ O(m))
        Space: O(n * k) to hold the repeated string (up to m + n chars)
        """
        n, m = len(A), len(B)
        # Quick impossible check (optional micro-optimization):
        # if any char in B not in A, early -1 (not sufficient but prunes many)
        if set(B) - set(A):
            return -1

        k = (m + n - 1) // n            # ceil(m / n)
        s = A * k
        if B in s:
            return k
        s += A                           # one more repeat to catch wrap-around
        if B in s:
            return k + 1
        return -1