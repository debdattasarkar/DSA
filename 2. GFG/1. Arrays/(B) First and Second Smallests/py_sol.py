#User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        #code here
        first = float('inf')
        second = float('inf')
    
        # Traverse through the array once
        for num in arr:
            if num < first:
                # New smallest found
                second = first
                first = num
            elif num < second and num != first:
                # New second smallest found
                second = num
    
        # If second is not updated, return -1
        if second == float('inf'):
            return [-1]
        else:
            return [first, second]
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        product = obj.minAnd2ndMin(arr)
        if product[0] == -1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends