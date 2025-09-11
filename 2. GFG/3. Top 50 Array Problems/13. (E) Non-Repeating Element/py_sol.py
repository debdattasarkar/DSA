#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        """
        Two-pass frequency approach.
        Time  : O(n)    (one count pass + one order-preserving pass)
        Space : O(n)    (hash map for frequencies)
        """
        # 1) Count frequencies in O(n)
        freq = Counter(arr)

        # 2) First element with freq==1 in original order
        for x in arr:                 # O(n)
            if freq[x] == 1:
                return x

        # No non-repeating element
        return 0