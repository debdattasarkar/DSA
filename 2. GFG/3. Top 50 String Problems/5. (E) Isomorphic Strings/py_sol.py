class Solution:
    def areIsomorphic(self, s1, s2):
        """
        Use two arrays of size 256 storing last-seen mapping (or -1).
        Time : O(n)
        Space: O(1)
        """
        if len(s1) != len(s2):
            return False

        M = 256
        fwd = [-1] * M   # s1 char -> s2 code
        rev = [-1] * M   # s2 char -> s1 code

        for c1, c2 in zip(s1, s2):
            i1, i2 = ord(c1), ord(c2)

            if fwd[i1] == -1 and rev[i2] == -1:
                fwd[i1] = i2
                rev[i2] = i1
            else:
                # must be consistent in both directions
                if fwd[i1] != i2 or rev[i2] != i1:
                    return False

        return True