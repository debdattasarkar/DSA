#User function Template for python3

class Solution:
    def nextPalin(self,N):
        n = len(N)
        # For length <= 3, it’s impossible to get a bigger palindrome with same digits
        if n <= 3:
            return "-1"

        # 1) Split into left, middle (if odd), and implicit right
        left = list(N[:n//2])
        mid = N[n//2] if n % 2 else ""

        # 2) Try to do next permutation on left half
        if not self._next_permutation(left):
            return "-1"  # left was already the highest arrangement

        # 3) Mirror back to form the palindrome
        L = ''.join(left)
        ans = L + mid + L[::-1]
        return ans

    def _next_permutation(self, a):
        """
        In-place next permutation for list of chars.
        Returns True if next permutation exists, else False.
        """
        # Step 1: find pivot i with a[i] < a[i+1]
        i = len(a) - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        if i < 0:
            return False  # no next permutation

        # Step 2: find rightmost j with a[j] > a[i]
        j = len(a) - 1
        while a[j] <= a[i]:
            j -= 1

        # Step 3: swap
        a[i], a[j] = a[j], a[i]

        # Step 4: reverse the suffix
        l, r = i + 1, len(a) - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return True