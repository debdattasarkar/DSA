from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        # code here
        # Step 1: Build graph and in-degree count
        graph = defaultdict(list)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                    break
            else:
                # Check invalid case like ["abc", "ab"]
                if len(w1) > len(w2):
                    return ""

        # Step 2: Topological Sort using BFS
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        res = []

        while queue:
            ch = queue.popleft()
            res.append(ch)
            for nei in graph[ch]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return "".join(res) if len(res) == len(in_degree) else ""