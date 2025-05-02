class Solution:
    def reverseArray(self, arr):
        # code here
        # Initialize two pointers at the start and end
        left = 0
        right = len(arr) - 1
    
        while left < right:
            # Swap elements at left and right
            arr[left], arr[right] = arr[right], arr[left]
            left += 1  # move left pointer inward
            right -= 1  # move right pointer inward
        

#{ 
 # Driver Code Starts
import sys


def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())

    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()

        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]

        # Create a Solution object
        obj = Solution()

        # Reverse the array
        obj.reverseArray(arr)

        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")

        # Decrement the test case count
        tc -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends