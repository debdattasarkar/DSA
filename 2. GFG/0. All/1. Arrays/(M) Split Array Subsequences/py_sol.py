from collections import Counter, defaultdict
class Solution:
    def isPossible(self, arr, k):
        """
        Greedy:
          - freq[x]: counts of unused x
          - need[y]: how many subsequences currently need y next
        For each x in sorted arr:
          1) if possible, extend a waiting subsequence ending at x-1
          2) else, try to start a new subsequence of length k starting at x
          3) else, fail
        Time  : O(n) average (hash ops), Space : O(n)
        """
        if k <= 1:
            return True  # any singletons suffice

        freq = Counter(arr)           # counts of remaining
        need = defaultdict(int)       # how many subseqs want this next value

        for x in arr:
            if freq[x] == 0:
                continue  # already consumed

            # consume current x
            freq[x] -= 1

            # 1) prefer to extend an existing subsequence needing x
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1
                continue

            # 2) otherwise, try to start a new subsequence of length k at x
            can_start = True
            for nxt in range(x + 1, x + k):
                if freq[nxt] <= 0:
                    can_start = False
                    break
            if not can_start:
                return False

            # consume x+1..x+k-1 to form a new length-k chain
            for nxt in range(x + 1, x + k):
                freq[nxt] -= 1
            # this new chain now needs x+k next
            need[x + k] += 1

        return True