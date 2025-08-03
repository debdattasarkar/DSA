#User function Template for python3
class Solution:

	def constructLowerArray(self,arr):
		# code here
		def update(index, bit):
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def query(index, bit):
            result = 0
            while index > 0:
                result += bit[index]
                index -= index & -index
            return result

        # Coordinate compression
        sorted_unique = sorted(set(arr))
        index_map = {val: i+1 for i, val in enumerate(sorted_unique)}  # 1-based indexing for BIT

        bit = [0] * (len(sorted_unique) + 2)
        res = []

        # Traverse from right to left
        for num in reversed(arr):
            idx = index_map[num]
            res.append(query(idx - 1, bit))  # count of smaller elements
            update(idx, bit)

        return res[::-1]  # reverse to restore original order