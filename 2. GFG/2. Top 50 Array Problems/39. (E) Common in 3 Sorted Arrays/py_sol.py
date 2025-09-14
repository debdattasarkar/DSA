#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        """
        Three-pointer sweep with duplicate skipping.
        Time:  O(n1 + n2 + n3)
        Space: O(1) extra (besides the result list)
        Returns: list of common elements in non-decreasing order,
                 or [-1] if none.
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        ans = []

        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]

            # If all equal, record once and skip duplicates in all arrays
            if a == b == c:
                ans.append(a)
                val = a
                # advance i/j/k past all occurrences of 'val'
                while i < n1 and arr1[i] == val: i += 1
                while j < n2 and arr2[j] == val: j += 1
                while k < n3 and arr3[k] == val: k += 1
            else:
                # find current minimum value
                m = min(a, b, c)
                # advance any pointer(s) equal to the minimum, skipping duplicates
                if a == m:
                    va = a
                    while i < n1 and arr1[i] == va: i += 1
                if b == m:
                    vb = b
                    while j < n2 and arr2[j] == vb: j += 1
                if c == m:
                    vc = c
                    while k < n3 and arr3[k] == vc: k += 1

        return ans if ans else [-1]