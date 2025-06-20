from collections import Counter

class Solution:
    def validgroup(self, arr ,k):
        # Code here
        if len(arr) % k != 0:
            return False

        arr.sort()
        freq = Counter(arr)

        for num in arr:
            if freq[num] == 0:
                continue

            # Try to form a group starting at num
            for i in range(k):
                if freq[num + i] == 0:
                    return False
                freq[num + i] -= 1

        return True
