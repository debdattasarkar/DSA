#User function Template for python3
class Solution:
	def maxRepeating(self,k, arr):
		# code here
		freq = [0] * k  # Frequency array for elements 0 to k-1

        # Count frequency of each number in arr
        for val in arr:
            freq[val] += 1

        max_freq = -1
        result = -1

        for i in range(k):
            if freq[i] > max_freq:
                max_freq = freq[i]
                result = i
            elif freq[i] == max_freq and i < result:
                result = i  # Choose smaller number in case of tie

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxRepeating(k, arr)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends