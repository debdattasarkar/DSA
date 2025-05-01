#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
		# code here
		# Separate even and odd numbers
        evens = [x for x in arr if x % 2 == 0]
        odds = [x for x in arr if x % 2 == 1]
    
        # Sort both lists
        evens.sort()
        odds.sort()
    
        # Combine back into arr (in-place)
        arr[:] = evens + odds


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

        print("~")

# } Driver Code Ends