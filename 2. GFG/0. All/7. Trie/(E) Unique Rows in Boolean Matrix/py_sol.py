from typing import List

class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
    #complete the function
        seen = set()
        result = []

        for i in range(row):
            current_row = tuple(M[i])  # Convert list to tuple to make it hashable
            if current_row not in seen:
                seen.add(current_row)
                result.append(M[i])  # Keep as list for output
        return result