#User function Template for python3
from functools import lru_cache

class Solution:
	def tsp(self, cost):
		#Code here
		n = len(cost)
        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]
        dp[1][0] = 0  # start at city 0 with only 0 visited

        for mask in range(1, 1 << n):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                for v in range(n):
                    if mask & (1 << v):  # already visited
                        continue
                    next_mask = mask | (1 << v)
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v])

        full_mask = (1 << n) - 1
        return min(dp[full_mask][u] + cost[u][0] for u in range(n))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        cost = []
        for _ in range(n):
            cost.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.tsp(cost)
        print(ans)

# } Driver Code Ends