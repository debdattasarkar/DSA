#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        """
        Two-pointer sweep accumulating segment sums until a common element,
        then take the larger segment sum + the common value, once.

        Time:  O(m + n)  (single pass)
        Space: O(1)      (constant extra)
        """
        i = j = 0
        s1 = s2 = 0          # running sums for current segments
        ans = 0
        m, n = len(arr1), len(arr2)

        # Walk both arrays
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            elif arr2[j] < arr1[i]:
                s2 += arr2[j]
                j += 1
            else:
                # switch point (same value). Count it once.
                ans += max(s1, s2) + arr1[i]
                s1 = s2 = 0
                i += 1
                j += 1

        # Add leftover tail from the unfinished array
        while i < m:
            s1 += arr1[i]
            i += 1
        while j < n:
            s2 += arr2[j]
            j += 1

        ans += max(s1, s2)
        return ans