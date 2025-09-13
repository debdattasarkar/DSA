class Solution:
    def majorityElement(self, arr):
        # ---- Phase 1: Find a candidate by cancelling different pairs ----
        candidate = None
        count = 0
        for x in arr:
            if count == 0:
                candidate = x        # pick new candidate when counter drops to zero
                count = 1
            elif x == candidate:
                count += 1           # same as candidate → reinforce
            else:
                count -= 1           # different → cancel out

        # ---- Phase 2: Verify the candidate actually is a majority ----
        if candidate is None:
            return -1
        freq = sum(1 for x in arr if x == candidate)
        return candidate if freq > len(arr) // 2 else -1