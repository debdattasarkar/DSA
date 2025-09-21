class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        L = [-1] * n        # previous smaller index
        R = [n] * n         # next smaller index

        # 1) Previous smaller (strictly smaller)
        st = []
        for i, x in enumerate(arr):
            # Maintain increasing stack
            while st and arr[st[-1]] >= x:   # ensure STRICT smaller on the top
                st.pop()
            L[i] = st[-1] if st else -1
            st.append(i)

        # 2) Next smaller (strictly smaller)
        st.clear()
        for i in range(n - 1, -1, -1):
            x = arr[i]
            while st and arr[st[-1]] > x:    # ensure STRICT smaller to the right
                st.pop()
            R[i] = st[-1] if st else n
            st.append(i)

        # 3) Fill answers: ans[len-1] gets max of arr[i]
        ans = [0] * n
        for i in range(n):
            length = R[i] - L[i] - 1
            ans[length - 1] = max(ans[length - 1], arr[i])

        # 4) Propagate right-to-left so smaller windows inherit
        for k in range(n - 2, -1, -1):
            ans[k] = max(ans[k], ans[k + 1])

        return ans