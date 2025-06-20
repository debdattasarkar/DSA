import heapq

class Solution:
    def findSmallestRange(self, arr):
        # code here
        k = len(arr)
        n = len(arr[0])

        heap = []
        max_val = float('-inf')

        # Initialize heap with first element from each list
        for i in range(k):
            heapq.heappush(heap, (arr[i][0], i, 0))
            max_val = max(max_val, arr[i][0])

        best_range = [float('-inf'), float('inf')]

        while True:
            min_val, row, idx = heapq.heappop(heap)

            # Update range if smaller
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]

            # Move to next element in the same list
            if idx + 1 == n:
                break
            next_val = arr[row][idx + 1]
            heapq.heappush(heap, (next_val, row, idx + 1))
            max_val = max(max_val, next_val)

        return best_range


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends