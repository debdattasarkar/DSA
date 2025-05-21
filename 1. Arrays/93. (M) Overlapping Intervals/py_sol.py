class Solution:
	def mergeOverlap(self, arr):
		#Code here
		# Sort intervals based on start time
        arr.sort(key=lambda x: x[0])
        
        merged = []
        for interval in arr:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # no overlap
            else:
                # merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged