class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        for c in s:
            rows[cur_row] += c
            # Change direction if we're at top or bottom
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return ''.join(rows)
