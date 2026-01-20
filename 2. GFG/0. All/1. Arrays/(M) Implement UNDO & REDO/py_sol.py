class Solution:
    def __init__(self):
        # document as list of characters (efficient append/pop at end)
        self.document_chars = []

        # redo stack stores characters removed by undo
        self.redo_stack = []

        # (optional) we don't strictly need an undo stack if document is the source of truth,
        # but keeping it conceptually helps interviews; we'll keep it minimal here.
        # We'll just use document for undo operations.

    def append(self, x):
        # Time: O(1)
        # Append character to document
        self.document_chars.append(x)

        # New edit invalidates redo history
        # Time: O(1) to reset reference; clear list is O(r) but amortized fine
        self.redo_stack.clear()

    def undo(self):
        # Time: O(1)
        # Undo last append: remove last char if exists
        if self.document_chars:
            removed_char = self.document_chars.pop()
            # store removed char for redo
            self.redo_stack.append(removed_char)

    def redo(self):
        # Time: O(1)
        # Restore last undone char if exists
        if self.redo_stack:
            char_to_restore = self.redo_stack.pop()
            self.document_chars.append(char_to_restore)

    def read(self):
        # Time: O(n) to join current document
        return "".join(self.document_chars)