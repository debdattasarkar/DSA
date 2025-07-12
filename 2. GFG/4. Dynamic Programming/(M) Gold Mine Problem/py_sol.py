class Solution:
    def maxGold(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Create a dp table with same dimensions
        dp = [[0]*m for _ in range(n)]  # Time: O(n*m), Space: O(n*m)

        # Step 2: Traverse from rightmost column to left
        for col in range(m-1, -1, -1):  # O(m)
            for row in range(n):        # O(n)
                # Right
                right = dp[row][col+1] if col != m-1 else 0
                # Right-up
                right_up = dp[row-1][col+1] if row > 0 and col != m-1 else 0
                # Right-down
                right_down = dp[row+1][col+1] if row < n-1 and col != m-1 else 0

                # Max of the three directions + current cell's gold
                dp[row][col] = mat[row][col] + max(right, right_up, right_down)

        # Step 3: Answer is max in first column
        result = max(dp[row][0] for row in range(n))  # O(n)

        return result