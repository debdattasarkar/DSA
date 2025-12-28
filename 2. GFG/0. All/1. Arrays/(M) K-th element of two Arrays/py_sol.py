class Solution:
    def kthElement(self, a, b, k):
        # Ensure 'a' is the smaller array to minimize binary search range
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        m = len(b)

        # cutA can’t be less than k-m (otherwise cutB would exceed m)
        # cutA can’t exceed k or n
        low = max(0, k - m)
        high = min(k, n)

        NEG_INF = float("-inf")
        POS_INF = float("inf")

        # Binary search for correct cutA
        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA

            leftA = a[cutA - 1] if cutA > 0 else NEG_INF
            rightA = a[cutA] if cutA < n else POS_INF

            leftB = b[cutB - 1] if cutB > 0 else NEG_INF
            rightB = b[cutB] if cutB < m else POS_INF

            # Check if partition is valid
            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            # Too many taken from a -> move left
            if leftA > rightB:
                high = cutA - 1
            else:
                # Too few taken from a -> move right
                low = cutA + 1

        # Should never reach here if inputs are valid
        return -1