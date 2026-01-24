class Solution:
    def josephus(self, n, k):
        # winner_index is 0-based winner for current circle size
        winner_index = 0  # f(1) = 0

        # Build answer from size=2 to n using recurrence:
        # f(size) = (f(size-1) + k) % size
        for size in range(2, n + 1):
            winner_index = (winner_index + k) % size

        # Convert 0-based to 1-based
        return winner_index + 1