#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        result = 0
        for num in arr:
            result ^= num
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

        print("~")
# } Driver Code Ends