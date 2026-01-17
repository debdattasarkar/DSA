class Solution():
    def checkRedundancy(self, s):
        # Stack will store characters of expression
        stack = []

        # Operators that make parentheses meaningful
        operators = set("+-*/")

        for ch in s:
            if ch != ')':
                # Push everything until we find a closing bracket
                stack.append(ch)
            else:
                # We are closing a bracket: check what is inside (...)
                has_operator = False

                # Pop until we reach '('
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in operators:
                        has_operator = True

                # Pop the '(' itself
                if stack:
                    stack.pop()

                # If there was no operator inside, brackets are redundant
                if not has_operator:
                    return True

        return False