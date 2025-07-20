class Solution:
    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()

        def canPlaceCows(min_dist):
            count = 1
            last_pos = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = stalls[i]
                if count >= k:
                    return True
            return False

        left, right = 1, stalls[-1] - stalls[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceCows(mid):
                answer = mid
                left = mid + 1  # Try for larger min distance
            else:
                right = mid - 1  # Try smaller distance

        return answer
