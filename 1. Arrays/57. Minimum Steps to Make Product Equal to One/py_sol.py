#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        # code here 
        steps = 0
        neg_count = 0
        zero_count = 0

        for num in arr:
            if num == 0:
                zero_count += 1
                steps += 1  # change 0 to 1
            elif num > 0:
                steps += num - 1  # reduce to 1
            else:
                steps += abs(num) - 1  # raise to -1
                neg_count += 1

        # If negative count is odd and no zeros to flip sign
        if neg_count % 2 != 0 and zero_count == 0:
            steps += 2  # Convert one -1 to 1

        return steps



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.makeProductOne(arr,N))
        print("~")
# } Driver Code Ends