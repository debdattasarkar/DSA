class Solution:
    def evaluatePostfix(self, arr):
        """
        Evaluate Reverse Polish Notation.
        Time : O(n)  — single pass, constant work per token
        Space: O(n)  — stack of at most n/2 numbers

        Notes:
          - token '^' means exponent, so use '**'
          - division is FLOOR division: a // b
          - tokens that are not operators are integers (may be negative)
        """
        ops = {"+", "-", "*", "/", "^"}
        st = []

        for tok in arr:
            if tok not in ops:  # number (handles "-3", "42", etc.)
                st.append(int(tok))
                continue

            # pop in the right order: b is top, a is next
            b = st.pop()
            a = st.pop()

            if tok == "+":
                st.append(a + b)
            elif tok == "-":
                st.append(a - b)
            elif tok == "*":
                st.append(a * b)
            elif tok == "/":
                # floor division as per problem statement
                st.append(a // b)
            else:  # tok == "^"  (power, not XOR)
                st.append(a ** b)

        # valid expression guarantees exactly one value remains
        return st[-1]