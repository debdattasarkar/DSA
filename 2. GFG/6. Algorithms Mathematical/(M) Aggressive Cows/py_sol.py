class Solution:
    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()

        def canPlaceCows(min_gap):
            countCows = 1
            prev_stall_loc = 0
            no_of_stalls = len(stalls)
            for curr_stall_loc in range(1, no_of_stalls):
                if stalls[curr_stall_loc] - stalls[prev_stall_loc] >= min_gap:
                    countCows += 1
                    prev_stall_loc = curr_stall_loc
                if countCows >= k:
                    return True
            return False

        left, right = 0, stalls[-1] - stalls[0]
        maxGap = 0

        while left <= right:
            gap = (left + right) // 2
            if canPlaceCows(gap):
                maxGap = gap
                left = gap + 1  # Try for larger min distance
            else:
                right = gap - 1  # Try smaller distance

        return maxGap