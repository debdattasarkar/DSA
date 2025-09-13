class Solution:
    def startStation(self, gas, cost):
        # If total gas < total cost, impossible
        total = 0
        # Current tank since last 'start' candidate
        curr = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            # If we went negative, none of the indices from 'start'..'i' can be a start
            if curr < 0:
                start = i + 1      # next station becomes the new candidate
                curr = 0           # reset tank for next segment

        # Feasible iff the whole circle has nonnegative total diff
        return start if total >= 0 and start < len(gas) else -1