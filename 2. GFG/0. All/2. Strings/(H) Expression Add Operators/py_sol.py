class Solution:
    def findExpr(self, s, target):
        """
        Generate all expressions by inserting +, -, * so that they evaluate to target.
        - No leading zeros in any operand (except the single digit "0").
        - Return list sorted lexicographically (as many judges expect).

        Let n = len(s). We choose cut points to form the next operand s[pos:i+1].
        For the first operand, we *must not* place an operator before it.

        Time  : O(4^(n-1)) worst-case branching (tight enough for n<=9)
        Space : O(n) path + O(n) recursion depth
        """
        n = len(s)
        res = []

        def backtrack(pos, path, value, prev):
            """
            pos   : next index in s to consume
            path  : expression string so far
            value : evaluated value of 'path'
            prev  : value of the last operand in 'path' (signed), to fix on '*'
            """
            if pos == n:
                if value == target:
                    res.append(path)
                return

            # Extend with the next operand s[pos:i+1]
            num = 0
            for i in range(pos, n):
                # leading zero rule: break if the first digit is '0' and more digits follow
                if i > pos and s[pos] == '0':
                    break
                num = num * 10 + (ord(s[i]) - 48)  # parse int fast

                if pos == 0:
                    # First number: no operator in front
                    backtrack(i + 1, s[pos:i+1], num, num)
                else:
                    # '+'
                    backtrack(i + 1, path + '+' + s[pos:i+1], value + num, +num)
                    # '-'
                    backtrack(i + 1, path + '-' + s[pos:i+1], value - num, -num)
                    # '*': undo last operand, then add prev*num
                    backtrack(i + 1, path + '*' + s[pos:i+1],
                              value - prev + prev * num, prev * num)

        backtrack(0, "", 0, 0)
        res.sort()  # many judges want lexicographically smallest order
        return res