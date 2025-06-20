#User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):
        # code here 
        def isValid(mid):
            subarrays = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return subarrays <= K

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
        print("~")
# } Driver Code Ends