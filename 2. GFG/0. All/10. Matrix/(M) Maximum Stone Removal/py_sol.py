from collections import defaultdict, deque
class Solution:
    def maxRemove(self, stones):
        """
        Graph + BFS with row/column maps.
        Still O(n^2) worst-case, but usually much faster.
        """
        n = len(stones)
        visited = [False] * n

        # Build maps from row and column to indices of stones
        row_to_indices = defaultdict(list)
        col_to_indices = defaultdict(list)
        for index, (row, col) in enumerate(stones):
            row_to_indices[row].append(index)
            col_to_indices[col].append(index)

        def bfs(start_index):
            queue = deque([start_index])
            visited[start_index] = True

            while queue:
                current = queue.popleft()
                r, c = stones[current]

                # All stones in the same row
                for neighbor in row_to_indices[r]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

                # All stones in the same column
                for neighbor in col_to_indices[c]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        component_count = 0
        for i in range(n):
            if not visited[i]:
                component_count += 1
                bfs(i)

        return n - component_count