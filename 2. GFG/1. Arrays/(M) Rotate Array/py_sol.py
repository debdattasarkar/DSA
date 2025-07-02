#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n  # In case d > n

        # Helper to reverse a subarray in-place
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse first d elements
        reverse(0, d - 1)

        # Step 2: Reverse rest of the array
        reverse(d, n - 1)

        # Step 3: Reverse the whole array
        reverse(0, n - 1)