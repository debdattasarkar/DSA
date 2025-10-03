#User function Template for python3

class Solution:
    def findString(self, N, K):
        """
        Robust De Bruijn construction via DFS on N-grams (edges).
        - Node = last (N-1) characters
        - Edge = N-gram formed by node + next digit
        We mark each edge exactly once (Eulerian), append digit on backtrack,
        and finally return start + reversed(collected digits).

        Time  : O(K^N)  (visits each N-gram once)
        Space : O(K^N)  (visited set + answer)
        """
        # N == 1 is a trivial base case: just 0..K-1
        if N == 1:
            return "".join(str(d) for d in range(K))

        # Start node of (N-1) zeros
        start = "0" * (N - 1)

        visited = set()   # stores used N-grams as strings (e.g., "01", "10", ...)
        ans = []          # digits appended on backtrack (will be reversed)

        def dfs(node: str):
            # Try digits in lexicographic order to get a canonical minimal answer
            for d in map(str, range(K)):
                edge = node + d
                if edge not in visited:
                    visited.add(edge)      # mark this N-gram as used
                    dfs(edge[1:])          # shift window by 1
                    ans.append(d)          # append the chosen digit on backtrack

        dfs(start)
        # Build the linear string: prefix (N-1 zeros) + reversed collected digits
        # Final length is exactly K^N + N - 1
        return start + "".join(reversed(ans))