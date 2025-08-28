class Solution:
    def maxOnes(self, arr, k):
        # code here
        # Longest subarray with at most k zeros (flip them → all 1s).
        n = len(arr)
        left = 0
        zeroes = 0
        best = 0

        for right in range(n):
            if arr[right] == 0:
                zeroes += 1  # we plan to flip this zero
            
            # If we exceeded k flips, shrink from the left
            while zeroes > k:
                if arr[left] == 0:
                    zeroes -= 1
                left += 1  # maintain feasibility

            # Update best with current feasible window length
            best = max(best, right - left + 1)

        return best
