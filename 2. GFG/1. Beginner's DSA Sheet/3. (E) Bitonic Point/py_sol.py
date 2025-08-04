#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		n = len(arr);
		left, right = 1, n -2
		while left <= right:
		    mid = (left + right) // 2
		    if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
		        return arr[mid]
		    elif arr[mid-1] < arr[mid]:
		        left = mid + 1
		    else:
		        right = mid - 1
		if right == 0:
		    return arr[0]
		return arr[n-1]