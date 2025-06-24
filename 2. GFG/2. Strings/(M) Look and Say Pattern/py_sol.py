class Solution:
    def countAndSay(self, n):
        # code here
        result = "1"
        for _ in range(n - 1):
            temp = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive identical digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                # Append count and digit to result
                temp += str(count) + result[i]
                i += 1
            result = temp
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends