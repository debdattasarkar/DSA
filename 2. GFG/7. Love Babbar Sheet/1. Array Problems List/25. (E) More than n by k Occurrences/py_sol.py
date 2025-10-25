class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        """
        Misra–Gries (generalized majority voting).
        Pass 1: keep at most (k-1) candidate elements with counters.
        Pass 2: verify real frequencies of remaining candidates.

        Time : O(n) for both passes combined
        Space: O(k)   (<= k-1 candidates)
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return 0
        if k == 1:
            # More than n/1 -> more than n occurrences (impossible)
            return 0

        # ------------- Pass 1: shortlist candidates -------------
        candidates = {}  # value -> count (not final frequencies)
        for x in arr:
            if x in candidates:
                candidates[x] += 1
            elif len(candidates) < k - 1:
                candidates[x] = 1
            else:
                # decrement every candidate; remove zeros
                to_del = []
                for v in candidates:
                    candidates[v] -= 1
                    if candidates[v] == 0:
                        to_del.append(v)
                for v in to_del:
                    del candidates[v]

        # ------------- Pass 2: verify true counts -------------
        # Count only for remaining candidates to keep O(k) memory.
        true_count = {v: 0 for v in candidates}
        for x in arr:
            if x in true_count:
                true_count[x] += 1

        threshold = n // k
        answer = sum(1 for v in true_count.values() if v > threshold)
        return answer