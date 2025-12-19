class Solution:
    def findMoves(self, chairs, passengers):
        """
        Optimized approach:
          1) Sort chairs and passengers
          2) Pair i-th passenger with i-th chair
          3) Sum absolute differences

        Time:
          Sorting chairs:     O(n log n)
          Sorting passengers: O(n log n)
          Pairing sum:        O(n)
          Total:              O(n log n)

        Space:
          If sorting in place: O(1) auxiliary (Python's sort has small overhead)
        """
        # Sort both lists so nearest-by-order positions match
        chairs.sort()
        passengers.sort()

        total_moves = 0

        # Sum distances between matched pairs
        for chair_pos, passenger_pos in zip(chairs, passengers):
            total_moves += abs(chair_pos - passenger_pos)

        return total_moves