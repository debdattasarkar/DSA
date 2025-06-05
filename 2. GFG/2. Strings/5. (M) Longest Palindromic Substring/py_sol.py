#User function Template for python3

class Solution:
    def longestPalindrome(self, s):
        # code here
        start, end = 0, 0

        for i in range(len(s)):
            # Odd-length palindromes
            l1, r1 = self.expandAroundCenter(s, i, i)
            # Even-length palindromes
            l2, r2 = self.expandAroundCenter(s, i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
        
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = input().strip()
        ob = Solution()
        print(ob.longestPalindrome(S))
        print("~")

# } Driver Code Ends