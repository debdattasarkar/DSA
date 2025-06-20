#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def findPairs(self, arr): 
        #code here.  
        # Dictionary to store frequency of pair sums
        sum_occurence = {}

        for i in range(len(arr)):
            # Remove the first element for this iteration
            val = arr.pop(0)

            # Iterate over the remaining elements
            for j in arr:
                pair_sum = val + j

                # Count the number of times this sum has occurred
                sum_occurence[pair_sum] = sum_occurence.get(pair_sum, 0) + 1

                # If any sum occurs more than once, it means two pairs exist with same sum
                if sum_occurence[pair_sum] == 2:
                    return True

        # If no matching pair sum found
        return False

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findPairs(arr)
        if(res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1


# } Driver Code Ends