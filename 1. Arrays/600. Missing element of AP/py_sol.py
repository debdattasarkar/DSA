#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        n = len(arr)

        # Step 1: Determine correct common difference (positive or negative)
        d = min(abs(arr[i+1] - arr[i]) for i in range(n - 1))
        # Determine if it's decreasing or increasing
        if arr[1] < arr[0]:
            d = -d

        # Step 2: Binary search to find mismatch
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            expected = arr[0] + mid * d
            if arr[mid] == expected:
                low = mid + 1
            else:
                high = mid

        # Step 3: Check if complete
        expected_last = arr[0] + (n - 1) * d
        if arr[-1] == expected_last:
            return arr[-1] + d  # Return next element
        else:
            return arr[0] + low * d  # Return missing element


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends