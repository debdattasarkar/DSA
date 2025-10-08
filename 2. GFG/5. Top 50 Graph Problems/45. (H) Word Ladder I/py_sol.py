class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		"""
        BFS on an implicit graph of words where edges connect words that differ by 1 letter.
        Optimization: wildcard buckets map (e.g., h*t) to all words matching that pattern,
        so neighbors can be fetched in O(#bucket) instead of scanning all words.

        Time:
          Build buckets:  O(N * M)  (N = len(wordList)+maybe startWord, M = word length)
          BFS traversal:  O(N * M)  (each word popped once; for each we touch M buckets)
        Space:
          Buckets + visited + queue: O(N * M)
        """
        # Edge cases
        if startWord == targetWord:
            return 1
        
        L = len(startWord)
        wordSet = set(wordList)
        # If target not in dictionary, no ladder is allowed by problem statement
        if targetWord not in wordSet:
            return 0
        # Ensure start is part of our world (helps when start not in list)
        wordSet.add(startWord)

        # Build wildcard buckets: key is word with one position replaced by '*'
        from collections import defaultdict, deque
        buckets = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                buckets[w[:i] + '*' + w[i+1:]].append(w)

        # Standard BFS from start
        q = deque([(startWord, 1)])
        visited = {startWord}

        while q:
            word, dist = q.popleft()
            if word == targetWord:
                return dist
            # Explore 1-change neighbors using wildcard keys
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                for nxt in buckets[key]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1))
                # Optional micro-opt: clear bucket so we never traverse it again
                buckets[key].clear()

        return 0