class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        rows = len(mat)
        cols = len(mat[0]) if rows else 0
        seen = set()

        for r in range(rows):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols):
                    # If current row has 1s in columns c1 and c2
                    if mat[r][c1] == 1 and mat[r][c2] == 1:
                        # Check if this pair has been seen before
                        if (c1, c2) in seen:
                            return True
                        # Mark this pair as seen
                        seen.add((c1, c2))
        return False