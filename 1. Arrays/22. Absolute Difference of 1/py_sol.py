#User function Template for python3

class Solution:
    
    def is_adjacent_diff_one(self, num):
        # Convert number to string to access digits
        digits = str(num)
        
        # Loop through adjacent digits and check their absolute difference
        for i in range(len(digits) - 1):
            if abs(int(digits[i]) - int(digits[i + 1])) != 1:
                return False  # If any pair fails, it's not valid
        return True  # All adjacent pairs passed
    
    def getDigitDiff1AndLessK(self, arr, k):
        # code here
        result = []
        for num in arr:
            if num < k and num >= 10 and self.is_adjacent_diff_one(num):
                result.append(num)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getDigitDiff1AndLessK(arr, k)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends