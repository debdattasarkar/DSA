class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []

        # Frequency map for current window
        frequency = {}

        # ---------- Step 1: Build frequency for first window ----------
        # Time: O(k), Space: O(k)
        for i in range(k):
            value = arr[i]
            frequency[value] = frequency.get(value, 0) + 1

        # Distinct count for first window
        result.append(len(frequency))

        # ---------- Step 2: Slide the window ----------
        # Each slide is O(1) average
        # Time: O(n-k), Space: O(k)
        for right in range(k, n):
            incoming = arr[right]         # new element entering window
            outgoing = arr[right - k]     # old element leaving window

            # Add incoming
            frequency[incoming] = frequency.get(incoming, 0) + 1

            # Remove outgoing
            frequency[outgoing] -= 1
            if frequency[outgoing] == 0:
                del frequency[outgoing]   # remove key to keep len(freq) correct

            # Distinct count in current window
            result.append(len(frequency))

        return result