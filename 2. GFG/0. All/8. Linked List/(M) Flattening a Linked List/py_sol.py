'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # ---------- Merge two sorted bottom-linked lists ----------
        # Time: O(a+b), Space: O(1) (iterative)
        def merge_sorted_bottom(list1, list2):
            dummy = Node(-1)
            tail = dummy

            while list1 and list2:
                if list1.data <= list2.data:
                    tail.bottom = list1
                    list1 = list1.bottom
                else:
                    tail.bottom = list2
                    list2 = list2.bottom

                tail = tail.bottom
                tail.next = None  # important: break next pointers in flattened list

            # Attach remaining nodes
            tail.bottom = list1 if list1 else list2

            # Ensure no next pointers remain in the final chain
            cur = dummy.bottom
            while cur:
                cur.next = None
                cur = cur.bottom

            return dummy.bottom

        # ---------- Base cases ----------
        if root is None or root.next is None:
            return root

        # Flatten the rest (right side)
        # Time: depends on total nodes, recursion depth up to n
        flattened_right = self.flatten(root.next)

        # Disconnect root.next because final answer uses bottom only
        root.next = None

        # Merge current column with flattened right
        return merge_sorted_bottom(root, flattened_right)