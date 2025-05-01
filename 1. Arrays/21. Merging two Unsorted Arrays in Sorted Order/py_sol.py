#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def sortedMerge(self, arr1,arr2,res):
        # Your code goes here
        merged = arr1 + arr2
        merged.sort()
        for i in range(len(merged)):
            res[i] = merged[i]  # update the res array in-place


#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        # First line contains the sizes of the arrays
        # Split the combined list into arr1 and arr2
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        n = len(arr1)
        m = len(arr2)

        res = [0] * (n + m)  # Initialize the result array with size n + m
        ob = Solution()
        ob.sortedMerge(arr1, arr2, res)

        # Print the merged array
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends