class Solution:
    def getSecondLargest(self, n):
        # Code Here
        n = list(set(n))
        if len(n) < 2:
            return -1
        n.sort(reverse=True)
        return n[1]