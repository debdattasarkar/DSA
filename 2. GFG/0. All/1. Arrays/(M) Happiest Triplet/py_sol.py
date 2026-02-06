class Solution:
    def smallestDiff(self,a, b, c):
        # Sort all arrays first
        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)

        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = [0, 0, 0]

        # Move pointers until one array ends
        while i < n1 and j < n2 and k < n3:
            x, y, z = a[i], b[j], c[k]

            current_min = min(x, y, z)
            current_max = max(x, y, z)
            diff = current_max - current_min
            s = x + y + z

            # Update best: smaller diff OR same diff but smaller sum
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                best_triplet = [x, y, z]

            # Move the pointer that has the minimum element
            # because increasing the minimum is the only way to shrink (max - min)
            if current_min == x:
                i += 1
            elif current_min == y:
                j += 1
            else:
                k += 1

        # Output must be in decreasing order
        best_triplet.sort(reverse=True)
        return best_triplet