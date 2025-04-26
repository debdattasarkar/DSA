#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        min_sum = curr_sum = A[0]
    
        for num in A[1:]:
            curr_sum = min(num, curr_sum + num)
            min_sum = min(min_sum, curr_sum)
    
        return min_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


            print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends