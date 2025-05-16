#User function Template for python3
class Solution:
    
    #Function to find the smallest window in the string s1 consisting
    #of all the characters of string s2.
    def smallestWindow(self, s1, s2):
        #code here
        from collections import Counter

        if not s1 or not s2:
            return ""

        target = Counter(s2)
        window = {}
        have, need = 0, len(target)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r, char in enumerate(s1):
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # shrink window
                window[s1[l]] -= 1
                if s1[l] in target and window[s1[l]] < target[s1[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s1[l:r+1] if res_len != float("inf") else ""


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import io
import atexit
from collections import defaultdict

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 = input().strip()  # Read the first string from a new line
        s2 = input().strip()  # Read the second string from the next line
        obj = Solution()
        str_res = obj.smallestWindow(s1, s2)
        if len(str_res) == 0:
            print("\"\"")
        else:
            print(str_res)
        print("~")

# } Driver Code Ends