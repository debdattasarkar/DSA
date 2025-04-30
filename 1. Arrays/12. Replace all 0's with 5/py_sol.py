# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        if n == 0:
            return 5

        result = 0
        place = 1
    
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5
            result += digit * place
            place *= 10
            n //= 10
    
        return result


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
# } Driver Code Ends