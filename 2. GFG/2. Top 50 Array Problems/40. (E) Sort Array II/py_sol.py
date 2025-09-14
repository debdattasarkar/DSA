class Solution:
    def sortArr(self, arr): 
        """
        Top-down merge sort (stable).
        Time:  O(n log n)
        Space: O(n) for temp arrays
        """
        def merge_sort(a):
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])
            # merge two sorted lists
            i = j = 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out

        res = merge_sort(arr)
        # copy back to keep the same "in-place" signature style
        arr[:] = res
        return arr