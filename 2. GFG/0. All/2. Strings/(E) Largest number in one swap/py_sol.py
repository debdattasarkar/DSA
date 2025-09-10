class Solution:
    def largestSwap(self, s):
        """
        Greedy: for each i, if any bigger digit exists to the right,
        swap with its RIGHTMOST occurrence and finish.
        Time:  O(n + 10*n) -> O(n)
        Space: O(1)  (array of size 10)
        """
        n = len(s)
        arr = list(s)

        # last[d] = rightmost index of digit d
        last = [-1] * 10
        for i, ch in enumerate(arr):                      # O(n)
            last[ord(ch) - 48] = i

        # left-to-right: try to improve position i
        for i, ch in enumerate(arr):                      # O(n)
            d = ord(ch) - 48
            # try larger digits from 9 down to d+1
            for b in range(9, d, -1):                     # at most 9 checks
                j = last[b]
                if j > i:                                 # larger digit exists to the right
                    arr[i], arr[j] = arr[j], arr[i]       # one swap
                    return "".join(arr)                   # done (at most one swap)
        return s  # already optimal