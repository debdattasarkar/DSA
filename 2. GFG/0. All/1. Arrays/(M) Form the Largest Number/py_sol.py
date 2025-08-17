class Solution:

	def findLargest(self, arr):
	    # code here
	     # Convert all numbers to strings once
        strs = list(map(str, arr))

        # Custom comparator: order x before y if x+y > y+x
        def cmp(x, y):
            if x + y > y + x:
                return -1     # x should come first
            elif x + y < y + x:
                return 1      # y should come first
            else:
                return 0      # equal preference

        # Sort using the comparator
        strs.sort(key=cmp_to_key(cmp))

        # Edge case: if the largest element is "0", all are zeros
        if strs[0] == "0":
            return "0"

        # Join into the largest number string
        return "".join(strs)