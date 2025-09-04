#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # Sort both. Sorting cost dominates.
        a.sort()
        b.sort()

        i = j = 0
        n, m = len(a), len(b)

        # Walk both arrays
        while i < n and j < m:
            if a[i] == b[j]:
                # Found one occurrence for b[j]; move both
                i += 1
                j += 1
            elif a[i] < b[j]:
                # Current a[i] is too small; skip it
                i += 1
            else:
                # a[i] > b[j] => the needed b[j] doesn't exist in 'a'
                return False

        # If we've matched all of b, it's a subset
        return j == m

