#User function Template for python3

class Solution:
    def getStar(self, arr):
        # code here
        n = len(arr)
        maxRight = float('-inf')
        writeIdx = 0  # Tracks where to write star elements

        for i in range(n - 1, -1, -1):
            if arr[i] > maxRight:
                arr[writeIdx] = arr[i]  # Write star element at front
                writeIdx += 1
                maxRight = arr[i]

        # Reverse the star elements portion
        return arr[:writeIdx][::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getStar(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends