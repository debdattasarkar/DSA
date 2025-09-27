class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        hint = [0] * n      # hint[i] == 1 → a flip starts at i
        cur = 0             # parity of active flips affecting current index
        ans = 0

        for i in range(n):
            # Remove effect of a flip that started at i-k (if any)
            if i >= k:
                cur ^= hint[i - k]

            # Effective bit after cur flips
            effective = arr[i] ^ cur

            if effective == 0:           # need to flip starting here
                if i + k > n:
                    return -1            # window would overflow → impossible
                ans += 1
                cur ^= 1                 # starting a new flip toggles parity
                hint[i] = 1              # remember: this flip will expire at i+k

        return ans