from functools import cmp_to_key
class Solution:

	def findLargest(self, arr):
	    # Interview-expected: custom comparator sort
        # Time: O(n log n * k), Space: O(n)

        numbers_as_strings = list(map(str, arr))

        def compare(a, b):
            # return -1 if a should come before b
            # return  1 if b should come before a
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        # Sort using the comparator
        numbers_as_strings.sort(key=cmp_to_key(compare))

        result = "".join(numbers_as_strings)

        # If the largest starts with '0', then all are zeros
        return "0" if result[0] == "0" else result