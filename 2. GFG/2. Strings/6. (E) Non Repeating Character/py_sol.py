class Solution:
    def nonRepeatingChar(self,s):
        #code here
        # Step 1: Frequency dictionary
        freq = [0] * 26  # for 'a' to 'z'

        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Step 2: Find first character with frequency 1
        for char in s:
            if freq[ord(char) - ord('a')] == 1:
                return char

        return '$'  # No non-repeating character
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")

# } Driver Code Ends