#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def numberofElementsInIntersection(self,a, b):
        #return: expected length of the intersection array.
        #code here
        set_b = set(b)          # Store b in set for fast lookup
        count = 0

        for num in a:
            if num in set_b:
                count += 1
                set_b.remove(num)  # To maintain distinct count

        return count


#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.
t = int(input().strip())
while t > 0:
    t -= 1
    # Read first array
    a = list(map(int, input().strip().split()))

    # Read second array
    b = list(map(int, input().strip().split()))

    #input()  # to consume the empty line

    # ADD Solution initialization
    sln = Solution()

    # Assuming numberofElementsInIntersection function is defined in Solution
    print(sln.numberofElementsInIntersection(a, b))
    print("~")

# } Driver Code Ends