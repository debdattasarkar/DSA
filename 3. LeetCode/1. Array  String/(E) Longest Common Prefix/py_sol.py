class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Assume the first string is the prefix
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Trim the last character
                if not prefix:
                    return ""
        return prefix