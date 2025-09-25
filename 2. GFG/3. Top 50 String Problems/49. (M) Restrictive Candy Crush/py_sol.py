#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        """
        Stack of (char, count).
        Time:  O(n)  -- each char pushed once and popped at most once
        Space: O(n)  -- worst-case (no removals)
        """
        if k <= 1 or not s:
            return ""  # k==1 removes everything; empty s stays empty

        st = []  # each element is [char, count]

        for ch in s:  # O(n)
            if st and st[-1][0] == ch:
                st[-1][1] += 1           # increment top count
                if st[-1][1] == k:
                    st.pop()              # remove the k-group
            else:
                st.append([ch, 1])        # start a new run

        # rebuild answer
        # NOTE: use list-join (O(n)), avoid repeated string concatenation (O(n^2))
        return "".join(c * cnt for c, cnt in st)