#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        # Convert to base-26 with digits 0..25 by using N-1 each step.
        # Time: O(log_26 N)  |  Space: O(log_26 N) for the output list/string
        if N <= 0:
            return ""  # (Out of scope per constraints, but safe.)
        
        out = []
        while N > 0:
            N -= 1                       # shift to 0..25
            r = N % 26                   # remainder in 0..25
            out.append(chr(ord('A') + r))# map 0->A, 25->Z
            N //= 26                     # move to next place
        out.reverse()
        return "".join(out)