#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        low = 0
        high = len(arr) - 1

        while low <= high:
            # If the subarray is already sorted, the lowest element is at index low
            if arr[low] <= arr[high]:
                return low

            mid = (low + high) // 2
            next_idx = (mid + 1) % len(arr)
            prev_idx = (mid - 1 + len(arr)) % len(arr)

            # Check if mid is the minimum element
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                return mid
            elif arr[mid] <= arr[high]:
                high = mid - 1  # Minimum is in the left part
            else:
                low = mid + 1   # Minimum is in the right part
        return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends