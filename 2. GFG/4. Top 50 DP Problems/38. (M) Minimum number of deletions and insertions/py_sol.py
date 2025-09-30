#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# Make the second dimension the smaller one for less space
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        n, m = len(s1), len(s2)

        prev = [0]*(m+1)  # dp for previous row (O(m) space)
        for i in range(1, n+1):
            cur = [0]*(m+1)
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur

        L = prev[m]
        return (n - L) + (m - L)