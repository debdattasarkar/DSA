class Solution:
	def countSubstring(self, s):
		# code here
		from collections import Counter
        count = Counter(s)
        ans = 0
        for freq in count.values():
            # Each character contributes freq substrings of length 1
            # and (freq * (freq - 1)) // 2 substrings with same start & end
            ans += freq * (freq + 1) // 2
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends