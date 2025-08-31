class Solution:
    def nextLargerElement(self, arr):
        # code here
        """
        Monotonic decreasing stack (values) scanning from right to left.
        For current x, pop all <= x; the new top (if any) is the next greater.
        Time:  O(n)   — each element pushed and popped at most once
        Space: O(n)   — worst-case stack + output
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # stack of candidate values (strictly decreasing)

        # Process from right to left so that the stack only contains elements to the right
        for i in range(n - 1, -1, -1):
            x = arr[i]
            # Remove those that cannot be next greater for x
            while st and st[-1] <= x:
                st.pop()
            # Next greater is now top (if any)
            if st:
                ans[i] = st[-1]
            # Push current element to become a candidate for the elements to the left
            st.append(x)

        return ans