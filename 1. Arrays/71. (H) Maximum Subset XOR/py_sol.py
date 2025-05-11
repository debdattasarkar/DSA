# function to return maximum XOR subset in set[]

class Solution:
    def maxSubsetXOR(self, arr, N):
        # add code here
        index = 0  # index of the current basis element

        # Go through each bit from 31 down to 0
        for i in range(31, -1, -1):
            maxInd = index
            maxEle = -1

            # Find the max element with i-th bit set
            for j in range(index, N):
                if (arr[j] & (1 << i)) and arr[j] > maxEle:
                    maxEle = arr[j]
                    maxInd = j

            if maxEle == -1:
                continue  # No element found with i-th bit set

            # Place it at the current index
            arr[index], arr[maxInd] = arr[maxInd], arr[index]

            # Eliminate the i-th bit from all others
            for j in range(N):
                if j != index and (arr[j] & (1 << i)):
                    arr[j] ^= arr[index]

            index += 1

        # Final XOR of all basis elements gives max subset XOR
        result = 0
        for i in range(index):
            result ^= arr[i]
        return result

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        obj = Solution()
        print(obj.maxSubsetXOR(set,n))

        print("~")
# } Driver Code Ends