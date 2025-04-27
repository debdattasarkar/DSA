#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

    def maxProduct(self,arr):
        # code here
        first = second = -1
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return first * second

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxProduct(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends