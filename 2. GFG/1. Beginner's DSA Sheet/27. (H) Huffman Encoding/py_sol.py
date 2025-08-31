# User function Template for python3
import heapq

# Node for Huffman tree
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''              # '0' when chosen as left, '1' as right

    # Let heapq order nodes by frequency
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Preorder DFS: append code only at leaves
def _collect_codes_preorder(ans, nd, path=''):
    new_path = path + nd.huff
    if nd.left:
        _collect_codes_preorder(ans, nd.left, new_path)
    if nd.right:
        _collect_codes_preorder(ans, nd.right, new_path)
    if not nd.left and not nd.right:
        ans.append(new_path)

class Solution:
    def huffmanCodes(self,S,f,N):
        # Build initial min-heap of leaf nodes
        heap = []
        for i in range(N):
            heapq.heappush(heap, node(f[i], S[i]))

        # Edge case: single symbol → code "0"
        if N == 1:
            return ["0"]

        # Repeatedly merge two minimum-frequency nodes
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            left.huff, right.huff = '0', '1'
            parent = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            heapq.heappush(heap, parent)

        # Preorder list of codes at leaves
        ans = []
        _collect_codes_preorder(ans, heap[0])
        return ans