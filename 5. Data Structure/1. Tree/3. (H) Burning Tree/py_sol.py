class Solution:
    def minTime(self, root, target):
        # code here
        def map_parents(node, parent_map):
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                if curr.left:
                    parent_map[curr.left] = curr
                    queue.append(curr.left)
                if curr.right:
                    parent_map[curr.right] = curr
                    queue.append(curr.right)

        def find_target(node, target):
            if not node:
                return None
            if node.data == target:
                return node
            return find_target(node.left, target) or find_target(node.right, target)

        parent_map = {}
        map_parents(root, parent_map)
        target_node = find_target(root, target)

        queue = deque([target_node])
        visited = set([target_node])
        time = 0

        while queue:
            size = len(queue)
            new_fire = False
            for _ in range(size):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        new_fire = True
            if new_fire:
                time += 1

        return time