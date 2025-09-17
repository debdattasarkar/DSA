#User function Template for python3

class Solution:
    def ReFormatString(self,S, K):
        """
        Time  : O(n)  – one pass to clean, one pass to slice/join
        Space : O(n)  – cleaned string + output
        """
        # 1) Remove dashes, uppercase
        clean = S.replace("-", "").upper()   # O(n)

        n = len(clean)
        if n == 0:
            return ""                        # nothing to format

        # 2) Determine first group length
        first = n % K
        if first == 0:
            first = K

        # 3) Collect groups
        parts = [clean[:first]]              # first group (1..K)
        # subsequent groups of exactly K chars
        for i in range(first, n, K):
            parts.append(clean[i:i+K])

        # 4) Join with dashes
        return "-".join(parts)