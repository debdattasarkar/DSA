#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        """
        Stable O(n) approach using auxiliary lists.
        Keeps the relative order of positives and negatives.
        Time  : O(n)
        Space : O(n)  (extra buffer to maintain stability)
        """
        positives = []  # will keep all >= 0 and > 0 as "positives" per problem text
        negatives = []

        # Single pass: partition stably into two lists
        for value in arr:
            if value >= 0:
                positives.append(value)
            else:
                negatives.append(value)

        # Overwrite the original list in-place (required by platform)
        arr[:] = positives + negatives
        # No return needed on GFG; but safe to keep as per many templates:
        return arr