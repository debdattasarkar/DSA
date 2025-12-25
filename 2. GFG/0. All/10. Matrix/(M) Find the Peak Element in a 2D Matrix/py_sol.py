class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        left_col = 0
        right_col = cols - 1
        
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            
            # 1) Find the row having maximum value in mid_col
            best_row = 0
            for r in range(1, rows):
                if mat[r][mid_col] > mat[best_row][mid_col]:
                    best_row = r
            
            current = mat[best_row][mid_col]
            
            # 2) Compare with left and right neighbors (out of bounds => -inf)
            left_neighbor = mat[best_row][mid_col - 1] if mid_col - 1 >= 0 else float("-inf")
            right_neighbor = mat[best_row][mid_col + 1] if mid_col + 1 < cols else float("-inf")
            
            # 3) If current is >= both, it's a peak
            if current >= left_neighbor and current >= right_neighbor:
                return [best_row, mid_col]
            
            # 4) Move towards the bigger neighbor
            if right_neighbor > current:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1
        
        return [-1, -1]