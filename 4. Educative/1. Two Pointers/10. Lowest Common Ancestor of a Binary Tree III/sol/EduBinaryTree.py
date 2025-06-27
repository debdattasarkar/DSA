from typing import List
from queue import Queue
from collections import deque
from EduTreeNode import *

class EduBinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if not nodes or nodes[0] is None:
            return None
        root = EduTreeNode(nodes[0])
        q = deque([root])
        i = 1
        while i < len(nodes):
            curr = q.popleft()
            if i < len(nodes) and nodes[i] is not None:
                curr.left = EduTreeNode(nodes[i])
                curr.left.parent = curr
                q.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                curr.right = EduTreeNode(nodes[i])
                curr.right.parent = curr
                q.append(curr.right)
            i += 1
        return root
    def find(self, root, value):
        if not root:
            return None
        q = deque([root])
        while q:
            currentNode = q.popleft()
            if currentNode.data == value:
                return currentNode
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        return None