# User function Template for Python3

from collections import deque

class Solution:
    def minThrow(self, N, arr):
        # code here
        # Build board mapping with ladders and snakes
        board = list(range(31))  # board[0] unused, board[i] = i by default
        for i in range(0, 2 * N, 2):
            board[arr[i]] = arr[i + 1]  # map start -> end

        visited = [False] * 31
        q = deque()
        q.append((1, 0))  # (current position, throw count)
        visited[1] = True

        while q:
            pos, throws = q.popleft()

            # Try all dice rolls from 1 to 6
            for die in range(1, 7):
                next_pos = pos + die
                if next_pos <= 30:
                    final_pos = board[next_pos]  # Apply snake/ladder
                    if final_pos == 30:
                        return throws + 1
                    if not visited[final_pos]:
                        visited[final_pos] = True
                        q.append((final_pos, throws + 1))
        return -1

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
        print("~")
# } Driver Code Ends
