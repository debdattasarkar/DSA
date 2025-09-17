class Solution:
    def decodedString(self, s):
        """
        Decode k[substring] with nesting using an explicit stack.

        Time  : O(n)   — each character is processed once
        Space : O(n)   — stack depth up to nesting level; plus output
        """
        curr = ""            # current decoded segment we are building
        num = 0              # current repeat count being read
        stack = []           # stores tuples: (previous_string, repeat)

        for ch in s:
            if ch.isdigit():
                # build multi-digit number: e.g., '12' -> 12
                num = num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                # entering a new bracket scope — save context
                stack.append((curr, num))
                curr = ""    # reset for the inner substring
                num = 0
            elif ch == ']':
                # leaving the current bracket scope — resolve repetition
                prev, repeat = stack.pop()
                curr = prev + curr * repeat
            else:
                # a-z letter — append to current segment
                curr += ch

        return curr