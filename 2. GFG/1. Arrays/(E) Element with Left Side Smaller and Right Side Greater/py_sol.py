class Solution:
    def findElement(self, arr):
        # code here
        n = len(arr)
        if n < 3:
            return -1

        # Step 1: Construct max_left array
        max_left = [0] * n
        max_left[0] = float('-inf')
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i - 1])

        # Step 2: Construct min_right array
        min_right = [0] * n
        min_right[-1] = float('inf')
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i + 1])

        # Step 3: Check the required condition
        for i in range(1, n - 1):  # Must exclude first and last elements
            if max_left[i] < arr[i] < min_right[i]:
                return arr[i]

        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1
        ob = Solution()
        ans = ob.findElement(arr)
        print(ans)
        print("~")
# } Driver Code Ends