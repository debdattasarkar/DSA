# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr):
        # Code here
        low = 0
        high = len(arr) - 1
    
        while low <= high:
            mid = (low + high) // 2
            
            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')
            
            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Peak found
            elif left > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    
        return -1  # Should never happen if input is valid

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends