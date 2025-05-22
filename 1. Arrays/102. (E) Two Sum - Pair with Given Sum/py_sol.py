#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		seen = set()
        for num in arr:
            if target - num in seen:
                return True  # Pair found
            seen.add(num)
        return False  # No pair found