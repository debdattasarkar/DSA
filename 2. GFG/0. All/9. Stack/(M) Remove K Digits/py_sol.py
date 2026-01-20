class Solution:
    def removeKdig(self, s, k):
        # Greedy + Monotonic stack
        # Time:  O(n)  (each digit pushed/popped at most once)
        # Space: O(n)  (stack)

        stack = []  # will store digits in increasing order as much as possible

        for ch in s:
            # While we can remove digits and last digit is bigger than current,
            # remove it to make number smaller earlier.
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If still need to remove digits, remove from end (largest suffix)
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Build string and remove leading zeros
        result = "".join(stack).lstrip("0")

        # If empty, return "0"
        return result if result else "0"