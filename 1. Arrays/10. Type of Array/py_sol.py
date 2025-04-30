#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def maxNtype(self , arr):
        #code here.
        n = len(arr)
        count_increases = 0
        count_decreases = 0
    
        # Count increases and decreases between adjacent elements
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                count_increases += 1
            elif arr[i] > arr[i + 1]:
                count_decreases += 1
    
        # Check for ascending
        if count_decreases == 0:
            return 1
        # Check for descending
        elif count_increases == 0:
            return 2
        # Check for ascending rotated: one drop and last element < first
        elif count_decreases == 1 and arr[-1] < arr[0]:
            return 4
        # Check for descending rotated: one rise and last element > first
        elif count_increases == 1 and arr[-1] > arr[0]:
            return 3
        else:
            return -1  # Not matching any defined type


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxNtype(arr)
        print(res)
        print("~");
        t -= 1


# } Driver Code Ends