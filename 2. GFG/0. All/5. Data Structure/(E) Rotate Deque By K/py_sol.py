from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        """
        Rotate using deque.rotate().
        - Normalize k by n.
        - For type=1 (right): rotate(+k)
          For type=2 (left) : rotate(-k)
        Time:  O(n) effective work to output/inspect; rotate itself is O(min(k, n-k)) in CPython.
        Space: O(1) extra (in-place on deque).
        Returns: list view of the rotated deque (common for graders).
        """
        n = len(dq)
        if n == 0:
            return []                      # safety, though constraints say n>=1
        k %= n
        if k == 0:
            return list(dq)

        # If input isn't a deque, convert temporarily
        was_list = not isinstance(dq, deque)
        if was_list:
            dq = deque(dq)

        if type == 1:          # right
            dq.rotate(+k)
        else:                  # type == 2 -> left
            dq.rotate(-k)

        return list(dq)        # standardize return type