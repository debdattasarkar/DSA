class Solution:
    def thirdLargest(self,arr):
        # code here
        # If less than 3 elements, return -1
        if len(arr) < 3:
            return -1
        
        # Sort in descending order
        arr.sort(reverse=True)
        
        # Return the third element (not unique)
        return arr[2]

#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))
        print("~")

# } Driver Code Ends