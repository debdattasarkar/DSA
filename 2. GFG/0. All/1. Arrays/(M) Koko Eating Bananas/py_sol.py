#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        # Code here
        from math import ceil

        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in arr)

        low, high = 1, max(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if hours_needed(mid) <= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer