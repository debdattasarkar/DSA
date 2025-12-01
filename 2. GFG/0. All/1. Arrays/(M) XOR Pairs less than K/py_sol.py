class TrieNode:
    def __init__(self):
        # children[0] for bit 0, children[1] for bit 1
        self.children = [None, None]
        # how many numbers pass through this node (subtree size)
        self.count = 0
class Solution:
    def __init__(self):
        # maximum bit position we care about (15 covers values up to 2^16-1)
        self.MAX_BIT = 15
    def cntPairs(self, arr, k):
        """
        Count number of pairs (i < j) such that arr[i] ^ arr[j] < k.

        Approach:
        - Maintain a binary Trie of previously seen numbers.
        - For each number x in arr (from left to right):
            * Query the Trie: how many previous y have x ^ y < k ?
            * Insert x into the Trie.
        - Sum all these counts.

        Time complexity:
            - For each of n numbers, we do:
                * query: O(#bits) = O(log MaxValue)
                * insert: O(#bits)
            -> Total O(n log MaxValue), with MaxValue <= 5*10^4 (≈ 16 bits)
        Space complexity:
            - Trie nodes: at most one node per distinct (prefix, bit) combination.
            - In worst case O(n * #bits) = O(n log MaxValue).
        """

        root = TrieNode()
        total_pairs = 0
        trie_built = False  # helps explain; not strictly required

        for value in arr:
            if trie_built:
                # Count how many previous numbers y satisfy value ^ y < k
                total_pairs += self._count_less_than(root, value, k)

            # Insert current value into the Trie, so it can pair with future numbers
            self._insert(root, value)
            trie_built = True

        return total_pairs
    # ---------- Trie insert ----------
    def _insert(self, root, number):
        """
        Insert 'number' into the binary Trie.

        Time  : O(#bits)
        Space : O(#bits) for new nodes (amortized)
        """
        node = root
        node.count += 1  # root also counts this number

        # Process bits from most significant to least significant
        for bit_pos in range(self.MAX_BIT, -1, -1):
            bit = (number >> bit_pos) & 1

            # Create child node if necessary
            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            # Move to child and increment its count
            node = node.children[bit]
            node.count += 1

    # ---------- Count y such that (number ^ y) < k ----------
    def _count_less_than(self, root, number, k):
        """
        Given the current Trie of previously inserted numbers,
        return count of numbers y such that (number ^ y) < k.

        Time : O(#bits)
        """
        node = root
        if node is None:
            return 0

        result = 0

        for bit_pos in range(self.MAX_BIT, -1, -1):
            if node is None:
                break  # no more numbers in this path

            bit_x = (number >> bit_pos) & 1
            bit_k = (k >> bit_pos) & 1

            if bit_k == 0:
                # XOR bit must be 0 (otherwise we'd exceed k at this position)
                # So y must have the same bit as x at this position.
                node = node.children[bit_x]
            else:
                # bit_k == 1

                # 1) Branch where XOR bit = 0 -> y_bit = bit_x
                #    This makes prefix < k because k has 1 here.
                #    So all numbers in that subtree are valid.
                same_child = node.children[bit_x]
                if same_child is not None:
                    result += same_child.count

                # 2) Branch where XOR bit = 1 -> y_bit = 1 - bit_x
                #    This keeps prefix equal to k, so we must continue exploring.
                node = node.children[1 - bit_x]

        return result