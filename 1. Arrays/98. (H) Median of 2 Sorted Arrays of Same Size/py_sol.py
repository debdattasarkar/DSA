#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        if len(a) > len(b):
            a, b = b, a  # Ensure a is the smaller array

        n = len(a)
        low, high = 0, n

        while low <= high:
            i = (low + high) // 2
            j = n - i

            aLeft = float('-inf') if i == 0 else a[i - 1]
            aRight = float('inf') if i == n else a[i]
            bLeft = float('-inf') if j == 0 else b[j - 1]
            bRight = float('inf') if j == n else b[j]

            if aLeft <= bRight and bLeft <= aRight:
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0
            elif aLeft > bRight:
                high = i - 1
            else:
                low = i + 1