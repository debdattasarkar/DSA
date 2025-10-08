#User function Template for python3
from collections import defaultdict, deque
from string import ascii_lowercase
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        """
        Returns all shortest transformation sequences from startWord to targetWord.

        Strategy:
          1) BFS by levels to discover the target at the first possible level.
             Build 'parents' mapping: child -> set of predecessors in previous level.
          2) When target is first reached, finish the current level, stop BFS.
          3) Backtrack (DFS) from target to start using 'parents' to enumerate all shortest paths.

        Time  : O(N * M * 26) for BFS neighbor-gen + output size (paths),
                where N = number of words in wordList (plus start), M = word length.
        Space : O(N * M) for structures + output paths.
        """
        word_set = set(wordList)
        if targetWord not in word_set:
            return []                       # Impossible to reach target

        word_set.add(startWord)             # Ensure start is allowed for adjacency
        L = len(startWord)

        # parents[w] = set of all previous-level words that can reach w in one step
        parents = defaultdict(set)

        q = deque([startWord])
        found = False

        # We remove words by level to allow multiple parents from the same level
        while q and not found:
            next_level = set()
            level_size = len(q)

            for _ in range(level_size):
                word = q.popleft()

                # Generate neighbors by single-character substitutions
                for i in range(L):
                    orig = word[i]
                    for ch in ascii_lowercase:
                        if ch == orig:
                            continue
                        nei = word[:i] + ch + word[i+1:]
                        if nei in word_set:             # unseen in previous levels
                            parents[nei].add(word)      # record parent
                            if nei not in next_level:   # enqueue once per level
                                next_level.add(nei)
                                q.append(nei)
                            if nei == targetWord:
                                found = True

            # Remove the whole level from the pool so deeper levels can't reuse them
            word_set -= next_level

        # If never reached target, no sequence exists
        if not found:
            return []

        # Backtrack all shortest paths from target -> start via 'parents'
        res, path = [], [targetWord]

        def dfs_backtrack(node):
            if node == startWord:
                res.append(path[::-1])  # reverse to get start -> ... -> target
                return
            for p in parents[node]:
                path.append(p)
                dfs_backtrack(p)
                path.pop()

        dfs_backtrack(targetWord)
        return res