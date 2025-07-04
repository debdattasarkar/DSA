# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr):
        # Code here
        # Binary Search based approach to find a peak element
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
                return mid
            # If the left neighbor is greater, then the peak lies on the left side
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            # If the right neighbor is greater, then the peak lies on the right side
            else:
                low = mid + 1
        
        # Return -1 if no peak is found (although per problem constraints, a peak always exists)
        return -1


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