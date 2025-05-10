#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Handle boundary safely
            if mid > 0 and mid < len(arr) - 1:
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return arr[mid]
                elif arr[mid] > arr[mid - 1]:
                    # still increasing
                    low = mid + 1
                else:
                    # decreasing
                    high = mid - 1
            elif mid == 0:
                return max(arr[0], arr[1])
            elif mid == len(arr) - 1:
                return max(arr[-1], arr[-2])

        return -1  # unreachable if input is valid

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends