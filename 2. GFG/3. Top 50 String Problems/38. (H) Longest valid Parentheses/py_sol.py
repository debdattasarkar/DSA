
class Solution:
    def maxLength(self, s):
        # Stack holds indices of characters.
        # Start with a "base" index (-1) to measure lengths easily.
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == '(':
                # Potential opener: push its index
                stack.append(i)
            else:
                # Closer: try to match by popping a previous '(' index
                stack.pop()
                if not stack:
                    # No base to measure from -> this ')' is invalid boundary
                    stack.append(i)
                else:
                    # Valid substring length = i - last_unmatched_index
                    best = max(best, i - stack[-1])

        return best