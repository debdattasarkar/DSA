from collections import deque
class Solution:
    def safeNodes(self, V, edges):
        # Build graph and reverse graph; also track outdegree in original graph
        graph = [[] for _ in range(V)]
        reverse_graph = [[] for _ in range(V)]
        outdeg = [0] * V

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)   # reversed edge
            outdeg[u] += 1

        # Start with all terminal nodes (outdegree 0)
        queue = deque([u for u in range(V) if outdeg[u] == 0])
        is_safe = [False] * V

        while queue:
            node = queue.popleft()
            is_safe[node] = True  # if we can peel it, it's safe
            # In reversed graph, go to predecessors in original graph
            for pred in reverse_graph[node]:
                outdeg[pred] -= 1              # remove edge pred->node
                if outdeg[pred] == 0:          # pred became terminal
                    queue.append(pred)

        # Safe nodes are those we peeled off (sorted because nodes are 0..V-1)
        return [i for i, safe in enumerate(is_safe) if safe]