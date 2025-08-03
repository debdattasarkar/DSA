#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    def printUnsorted(self, arr):
        # Code here
        n = len(arr)
        start, end = -1, -1

        # Step 1: Find the first index from the left where order breaks
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                start = i
                break

        if start == -1:
            return [0, 0]  # Already sorted

        # Step 2: Find the first index from the right where order breaks
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                end = i
                break

        # Step 3: Find min and max in the unsorted subarray
        sub_min = min(arr[start:end + 1])
        sub_max = max(arr[start:end + 1])

        # Step 4: Expand start and end if needed
        for i in range(start):
            if arr[i] > sub_min:
                start = i
                break

        for i in range(n - 1, end, -1):
            if arr[i] < sub_max:
                end = i
                break

        return [start, end]


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        sol = Solution()
        ans = sol.printUnsorted(arr)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends