class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_split = merge(left, right)
            return merged, inv_left + inv_right + inv_split

        def merge(left, right):
            i = j = inv_count = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i  # All remaining in left are > right[j]
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, count = merge_sort(arr)
        return count