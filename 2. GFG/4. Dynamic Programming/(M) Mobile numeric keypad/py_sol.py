class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
            return 10

        # Adjacency list
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize dp with size 10 for digits, n+1 for lengths
        dp = [[0]*(n+1) for _ in range(10)]

        for i in range(10):
            dp[i][1] = 1

        for l in range(2, n+1):
            for d in range(10):
                for m in moves[d]:
                    dp[d][l] += dp[m][l-1]

        return sum(dp[i][n] for i in range(10))