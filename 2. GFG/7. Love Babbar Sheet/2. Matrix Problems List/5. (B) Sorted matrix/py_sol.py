#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        """
        Flatten all N^2 elements, sort them, and refill row-wise.
        Time  : O(N^2 log N)          (sorting N^2 numbers)
        Space : O(N^2)                (flattened array)
        """
        # 1) Flatten
        flat = []
        for r in range(N):
            # append row to flat; each push is O(1)
            flat.extend(Mat[r])

        # 2) Sort the whole list
        flat.sort()  # Timsort: O(N^2 log N)

        # 3) Refill row-wise
        idx = 0
        for r in range(N):
            for c in range(N):
                Mat[r][c] = flat[idx]
                idx += 1

        return Mat