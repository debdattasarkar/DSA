class Solution:
    def findExtra(self,a,b):
        #add code here
        low, high = 0, len(b)  # b is shorter by 1

        while low <= high:
            mid = (low + high) // 2
            # Check if elements differ or we've gone past b
            if mid >= len(b) or a[mid] != b[mid]:
                high = mid - 1  # mismatch is before or at mid
            else:
                low = mid + 1  # matched so far, search right

        return low  # 'low' ends at index of extra element

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        # Take the first array as input
        arr1 = list(map(int, input().strip().split()))

        # Take the second array as input
        arr2 = list(map(int, input().strip().split()))

        # Create an instance of Solution and call the function
        ob = Solution()
        result = ob.findExtra(arr1, arr2)

        # Print the result
        print(result)

        tc -= 1
        print("~")

# } Driver Code Ends