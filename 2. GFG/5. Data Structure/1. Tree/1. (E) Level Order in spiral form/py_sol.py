'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

class Solution:
    def findSpiral(self, root):
        #code here
        if not root:
            return []

        # Two stacks for alternating levels
        s1 = [root]  # Right to Left
        s2 = []      # Left to Right

        result = []

        while s1 or s2:
            # Process s1: right to left
            while s1:
                node = s1.pop()
                result.append(node.data)
                # Push right then left
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)

            # Process s2: left to right
            while s2:
                node = s2.pop()
                result.append(node.data)
                # Push left then right
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)

        return result
        


#{ 
 # Driver Code Starts
from collections import deque


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while q and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)

        i += 1
    return root


# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends