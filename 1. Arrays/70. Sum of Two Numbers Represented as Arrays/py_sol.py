#User function Template for python3
class Solution:

	def findSum(self,arr1, arr2):
		# code here
		i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []

        # Add digits from end of both arrays
        while i >= 0 or j >= 0 or carry:
            digit1 = arr1[i] if i >= 0 else 0
            digit2 = arr2[j] if j >= 0 else 0
            total = digit1 + digit2 + carry

            result.append(total % 10)     # Add last digit of sum
            carry = total // 10           # Carry forward the remaining part

            i -= 1
            j -= 1

        result.reverse()  # Reverse to get the most significant digit first
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.findSum(arr1, arr2)
        print(*l)
        print("~")

# } Driver Code Ends