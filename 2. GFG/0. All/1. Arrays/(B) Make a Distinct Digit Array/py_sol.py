#User function Template for python3

class Solution:
	def common_digits(self, nums):
		# Code here
		digit_set = set()

        for num in nums:
            while num > 0:
                digit_set.add(num % 10)
                num //= 10
    
        return sorted(digit_set)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.common_digits(nums)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends