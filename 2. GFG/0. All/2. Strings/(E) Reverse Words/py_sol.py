#User function Template for python3

class Solution:
    def isPalindrome(self, n):
		# Code here
		strn = str(n)
		
		left, right = 0, len(strn)-1
		while left <= right:
		    if strn[left] != strn[right]:
		        return False
		    left += 1
		    right -= 1
		return True