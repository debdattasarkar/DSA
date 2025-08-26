class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        # Time: O(|s2|) average, Space: O(1)
        # Edge: empty s1 is subsequence of any s2
        if not s1:
            return True
        # Create an iterator over s2 and check characters of s1 in order
        it = iter(s2)  # O(1)
        # all(...) short-circuits: for each c in s1, keep consuming from s2
        return all(c in it for c in s1)  # each membership uses iterator progression