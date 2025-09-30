#User function Template for python3
from functools import lru_cache
class Solution:
    def countWays(self, s):
        """
        Memoized recursion on (i, j, wantTrue).

        Time:  O(n^3) states/transitions
        Space: O(n^2) memo + recursion depth O(n)
        """
        sym = s[::2]
        ops = s[1::2]
        n = len(sym)

        @lru_cache(maxsize=None)
        def solve(i, j, wantTrue):
            # Single symbol
            if i == j:
                val = (sym[i] == 'T')
                return 1 if val == wantTrue else 0

            ways = 0
            for k in range(i, j):  # split at op[k]
                op = ops[k]
                # Counts for left and right
                LT = solve(i, k, True)
                LF = solve(i, k, False)
                RT = solve(k + 1, j, True)
                RF = solve(k + 1, j, False)

                if op == '&':
                    if wantTrue:
                        ways += LT * RT
                    else:
                        ways += LT*RF + LF*RT + LF*RF
                elif op == '|':
                    if wantTrue:
                        ways += LT*RT + LT*RF + LF*RT
                    else:
                        ways += LF * RF
                else:  # '^'
                    if wantTrue:
                        ways += LT*RF + LF*RT
                    else:
                        ways += LT*RT + LF*RF
            return ways

        return solve(0, n - 1, True)