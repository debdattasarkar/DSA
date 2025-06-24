class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack = []
        n = len(s)
        keep = n - k  # we want to keep (n-k) characters
        
        for i, c in enumerate(s):
            while stack and k > 0 and stack[-1] < c:
                stack.pop()
                k -= 1
            stack.append(c)

        # Remove extra characters if k remains
        return ''.join(stack[:keep])
