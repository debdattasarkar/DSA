#User function Template for python3

class Solution:
    def hcf(self, a, b):
        # Recursive function to compute GCD (Euclidean algorithm)
        return a if b == 0 else self.hcf(b, a % b)  # Time: O(log min(a, b))

    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        """
        Rotate the array arr[] by d elements to the left using the Juggling algorithm.
        Time: O(n), Space: O(1)
        """
        n = len(arr)
        d = d % n  # Normalize d if it's >= n
        sets = self.hcf(n, d)

        for start in range(sets):
            curr = start
            temp = arr[curr]  # Store the first element in the current set

            while True:
                next_idx = (curr + d) % n

                if next_idx == start:
                    break

                arr[curr] = arr[next_idx]  # Move element from next_idx to curr
                curr = next_idx

            arr[curr] = temp  # Place temp in the final position of the cycle
        return arr