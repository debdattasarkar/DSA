#User function Template for python3

class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        """
        Linear-time strategy:
        1) Verify matches against the ORIGINAL S.
        2) Build a dict from start_index -> (len_source, target) for matches.
        3) Single pass over S: when i hits a matched index, append target and skip len_source.
                             else append S[i] and i += 1.
        Time  : O(|S| + sum(len(source_i)))
        Space : O(Q) for map + O(|S|) for output builder
        """
        n = len(S)
        # Step 1: record only the matches
        match = {}  # start_index -> (len_source, target)
        for i in range(Q):
            start = index[i]
            src   = sources[i]
            k     = len(src)
            if 0 <= start <= n - k and S[start:start + k] == src:
                match[start] = (k, targets[i])  # save verified match

        # Step 2: build the result
        ans = []
        i = 0
        while i < n:
            if i in match:
                k, repl = match[i]
                ans.append(repl)   # append target
                i += k             # skip the matched source portion
            else:
                ans.append(S[i])   # copy original char
                i += 1

        return "".join(ans)