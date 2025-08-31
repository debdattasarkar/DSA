class Solution:
    def catchThieves(self, arr, k):
        #code  here
        """
        Optimized two-pointer scan (O(n) time, O(1) space).
        Walk with two indices that always point to the next P and next T.
        """
        n = len(arr)
        i = j = 0          # i -> index of next 'P', j -> index of next 'T'
        caught = 0

        # helper lambdas to jump to next P/T in O(1) amortized per step
        def nextP(x):
            while x < n and arr[x] != 'P':
                x += 1
            return x

        def nextT(x):
            while x < n and arr[x] != 'T':
                x += 1
            return x

        i = nextP(i)
        j = nextT(j)

        while i < n and j < n:
            if abs(i - j) <= k:
                # match this policeman-thief pair
                caught += 1
                i = nextP(i + 1)   # move to next policeman
                j = nextT(j + 1)   # move to next thief
            elif i < j:
                # policeman is left of thief but too far -> this P can't catch any T to the right of j
                i = nextP(i + 1)
            else:
                # thief is left of policeman but too far -> this T can't be caught by any P to the right of i
                j = nextT(j + 1)

        return caught