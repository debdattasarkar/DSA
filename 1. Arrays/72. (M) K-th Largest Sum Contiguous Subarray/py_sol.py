from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        minHeap = []

        n = len(arr)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]

                if len(minHeap) < k:
                    heapq.heappush(minHeap, curr_sum)
                else:
                    if curr_sum > minHeap[0]:
                        heapq.heappushpop(minHeap, curr_sum)

        return minHeap[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends