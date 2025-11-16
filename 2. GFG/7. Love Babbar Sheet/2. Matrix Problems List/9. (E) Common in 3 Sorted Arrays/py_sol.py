#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        """
        Return distinct elements common to all three sorted arrays.
        If none exist, return [-1].

        Time:  O(n1 + n2 + n3)  -> single pass with three pointers
        Space: O(1) extra       -> only indices and output list
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        answer = []

        # Walk the three arrays simultaneously
        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]

            # Case 1: common value found
            if a == b == c:
                # Add once (distinct output)
                answer.append(a)

                # Move all three pointers forward while skipping duplicates
                current = a
                while i < n1 and arr1[i] == current:  # O(#dups1)
                    i += 1
                while j < n2 and arr2[j] == current:  # O(#dups2)
                    j += 1
                while k < n3 and arr3[k] == current:  # O(#dups3)
                    k += 1

            else:
                # Case 2: advance the smallest to catch up
                smallest = min(a, b, c)
                if a == smallest:
                    # Skip duplicates of arr1[i] while advancing
                    val = a
                    while i < n1 and arr1[i] == val:
                        i += 1
                elif b == smallest:
                    val = b
                    while j < n2 and arr2[j] == val:
                        j += 1
                else:  # c is smallest
                    val = c
                    while k < n3 and arr3[k] == val:
                        k += 1

        return answer if answer else [-1]