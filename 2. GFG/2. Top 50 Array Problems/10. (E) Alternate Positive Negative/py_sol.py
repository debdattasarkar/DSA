# User function Template for python3

class Solution:
    def rearrange(self, arr):
        """
        Stable split + merge, starting with positive (0 counts as positive).
        Time  : O(n)  (split + merge)
        Space : O(n)  (pos/neg buffers)
        IMPORTANT: overwrite 'arr' by index so the driver sees the change.
        """
        pos = [x for x in arr if x >= 0]   # keep order
        neg = [x for x in arr if x < 0]    # keep order

        i = j = k = 0

        # Alternate: +, -, +, -, ...
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i];  i += 1;  k += 1
            arr[k] = neg[j];  j += 1;  k += 1

        # Append remainder (still stable)
        while i < len(pos):
            arr[k] = pos[i];  i += 1;  k += 1
        while j < len(neg):
            arr[k] = neg[j];  j += 1;  k += 1
