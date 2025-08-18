class Solution:
    def hIndex(self, citations):
        # Time: O(n)
        # Space: O(n)
        n = len(citations)
        bucket = [0] * (n + 1)
        
        # Count how many papers have exactly c citations (capped at n)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        
        # Suffix accumulation to find largest h such that
        # at least h papers have >= h citations
        papers = 0
        for h in range(n, -1, -1):   # n, n-1, ..., 0
            papers += bucket[h]
            if papers >= h:
                return h
        return 0