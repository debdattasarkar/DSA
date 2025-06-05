#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longest(self, arr):
        #Code Here
        n = len(arr)
    
        # base case
        if n == 0:
            return 0
        
        # Answer is set to zero
        ans = 0
        
        for i in range(n):
            maxi = True
            
            for j in range(i):
                if arr[j] > arr[i]:
                    maxi = False
                    break
            
            if maxi:
                ans += 1
        
        return ans

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longest(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends