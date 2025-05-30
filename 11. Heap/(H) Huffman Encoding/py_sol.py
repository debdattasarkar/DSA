#User function Template for python3
# User function Template for python3
import heapq  # Importing heapq to use a min-heap (priority queue)

# Node class for the Huffman Tree
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq              # Frequency of the symbol
        self.symbol = symbol          # Character/symbol
        self.left = left              # Left child node
        self.right = right            # Right child node
        self.huff = ''                # Huffman code bit to add (0 or 1)

    # Comparison method for heapq to sort based on frequency
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Recursive function to extract Huffman codes from the tree
def getList(ans, node, val=''):
    newval = val + str(node.huff)  # Accumulate the Huffman code path
    if node.left:                  # Traverse left subtree
        getList(ans, node.left, newval)
    if node.right:                 # Traverse right subtree
        getList(ans, node.right, newval)
    if not node.left and not node.right:  # If it's a leaf node
        ans.append(newval)                # Add its code to result list
        
class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        # Step 1: Initialize a min-heap with all characters and their frequencies
        nodes = []
        for x in range(len(S)):
            heapq.heappush(nodes, node(f[x], S[x]))  # Push node into heap

        # Step 2: Build the Huffman Tree
        while len(nodes) > 1:
            # Pop two nodes with lowest frequency
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            # Assign binary codes
            left.huff = '0'
            right.huff = '1'

            # Merge them into a new internal node with combined frequency
            newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            heapq.heappush(nodes, newnode)  # Push merged node back into heap

        # Step 3: Extract the codes from the final Huffman tree
        ans = []
        getList(ans, nodes[0])  # Start DFS from the root of the tree
        return ans  # Return the list of Huffman codes