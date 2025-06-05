class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	squares = set(x * x for x in arr)
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] * arr[i] + arr[j] * arr[j]
                if s in squares:
                    return True
        return False