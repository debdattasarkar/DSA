#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        """
        Build a trie for all dictionary words, then DFS from each cell following
        only valid trie prefixes. Add a word when we hit a trie node with is_end=True.

        Let R,C = board dims, D = number of words, L = avg word length.
        Time  : O(R*C * 8^L_pruned) in practice; upper bound O(R*C*8^L) but
                trie prefix-pruning makes it fast.
                Trie build is O(sum |w|) = O(D*L).
        Space : O(D*L) for trie + O(L) recursion + O(R*C) for visited flags.
        """
        if not board or not board[0] or not dictionary:
            return []

        R, C = len(board), len(board[0])

        # --- Build trie ---
        # Each node: {"children": {ch:node}, "end": False}
        def new_node():
            return {"ch": {}, "end": False}
        root = new_node()

        for w in dictionary:
            node = root
            for ch in w:
                if ch not in node["ch"]:
                    node["ch"][ch] = new_node()
                node = node["ch"][ch]
            node["end"] = True

        res = set()  # set to avoid duplicates if multiple paths form same word
        visited = [[False]*C for _ in range(R)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 neighbors

        def dfs(r, c, node, path):
            ch = board[r][c]
            if ch not in node["ch"]:         # prefix pruning
                return
            nxt = node["ch"][ch]
            path.append(ch)
            visited[r][c] = True
            if nxt["end"]:
                res.add("".join(path))       # whole word found

            # explore neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    # only proceed if neighbor char is a child in trie (fast check)
                    if board[nr][nc] in nxt["ch"]:
                        dfs(nr, nc, nxt, path)

            visited[r][c] = False
            path.pop()

        # Start DFS from each cell if it is a possible prefix
        # micro-optimization: pre-check char existence at root
        root_children = root["ch"]
        for i in range(R):
            for j in range(C):
                if board[i][j] in root_children:
                    dfs(i, j, root, [])

        return sorted(res)  # lexicographical order as required