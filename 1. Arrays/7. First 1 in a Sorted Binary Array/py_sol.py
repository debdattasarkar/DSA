#{ 
 # Driver Code Starts

# } Driver Code Ends

#User function Template for python3

class Solution:
    def firstIndex(self, arr):
    # Your code goes here
        low, high = 0, len(arr) - 1
        answer = -1
    
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 1:
                answer = mid
                high = mid - 1  # search on the left side for earlier 1
            else:
                low = mid + 1
        return answer



#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.firstIndex(arr))
        print("~")
# } Driver Code Ends