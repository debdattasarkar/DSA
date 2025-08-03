#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                result = mid        # Record position
                high = mid - 1      # Search left for first occurrence
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return result


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends