class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def count_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),         (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Consider 1 and -1 as live (before update)
                    if abs(board[nr][nc]) == 1:
                        count += 1
            return count

        # First pass: mark changes with temp values
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_neighbors(r, c)

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # 1 -> 0
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2   # 0 -> 1

        # Second pass: finalize
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0