class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        # Convert array to a set for O(1) average lookup time
        elements = set(arr)
    
        # Check every number from A to B is present in the set
        for i in range(A, B + 1):
            if i not in elements:
                return False  # If any number is missing, return False
        return True  # All numbers in range A to B are present


#{ 
 # Driver Code Starts
if __name__ == '__main__':

    t = int(input())
    for _ in range(0, t):
        l = list(map(int, input().split()))
        n = l[0]
        k = l[1]
        y = l[2]
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.check_elements(a, n, k, y)
        if (ans):
            print("True")
        else:
            print("False")
        print("~")

# } Driver Code Ends