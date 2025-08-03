
class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False  # Mismatch or empty stack
                stack.pop()
            else:
                continue  # Ignore other characters if any

        return len(stack) == 0  # Stack should be empty if valid