#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        s = list(s)
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        s = ''.join(s)
        return s