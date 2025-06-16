from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i  # First time citation is less than position
        return len(citations)  # All values >= positions