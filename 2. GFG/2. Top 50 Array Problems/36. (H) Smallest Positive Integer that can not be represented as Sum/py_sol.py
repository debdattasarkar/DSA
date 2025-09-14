#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        """
        Greedy coverage:
          - Keep 'miss' = smallest sum NOT yet representable (initially 1).
          - For each x in sorted array:
              if x <= miss: extend coverage to [1 .. miss + x), so miss += x
              else: break; 'miss' is the answer.
        Time:  O(n log n) for sort + O(n) scan
        Space: O(1) extra (in-place sort + a few scalars)
        """
        array.sort()                 # O(n log n)
        miss = 1                     # smallest not yet representable

        for x in array:              # O(n)
            if x > miss:
                break                # we cannot form 'miss'
            miss += x                # extend reachable range

        return miss