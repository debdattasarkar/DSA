
class Solution:
    def longestPalindrome(self, s):
        # code here
        start, end = 0, 0
        
        # Helper function to expand around the center
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindromes
            l1, r1 = expandAroundCenter(i, i)
            # Even-length palindromes
            l2, r2 = expandAroundCenter(i, i + 1)
            
            # Choose the longer
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends