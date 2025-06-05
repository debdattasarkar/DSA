#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        # Traverse from the end to the start of the array
        for i in reversed(range(N)):
            if arr[i] < 9:
                arr[i] += 1  # Add 1 and stop if no carry needed
                return arr
            arr[i] = 0  # Set to 0 and continue to propagate the carry
        
        # If we exited the loop, all digits were 9 (e.g. 999 -> 1000)
        return [1] + [0] * N  # Add leading 1 and N zeroes


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
        print("~")
# } Driver Code Ends