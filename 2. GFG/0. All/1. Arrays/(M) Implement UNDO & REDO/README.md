# Implement UNDO & REDO

**Difficulty:** Medium
**Accuracy:** 79.49%
**Submissions:** 2K+
**Points:** 4

---

## Problem Statement

You are given a text document that is initially empty. You need to complete the following functions:

* `void append(char x)` – Append the character `x` to the end of the document.
* `void undo()` – Undo the most recent **APPEND** operation (remove the last appended character).
* `void redo()` – Reapply the most recent undone operation (restore the last character removed by **UNDO**).
* `string read()` – Return the current content of the document as a string.

---

## Queries

There will be a sequence of `q` queries `arr[]` on the document. The queries are represented in numeric form:

* `1 x` → Call `append(x)`
* `2` → Call `undo()`
* `3` → Call `redo()`
* `4` → Call `read()`

The driver code will process the queries, call the corresponding functions, and finally print the outputs of all `READ()` operations.

You only need to implement the above four functions.

---

## Examples

### Example 1

**Input:**
`arr[] = [[1 'A'], [1 'B'], [1 'C'], [2], [4], [3], [4]]`

**Output:**
`["AB", "ABC"]`

**Explanation:** For each query following changes are made into the document.
1st query: Append('A'), Document contains `"A"`.
2nd query: Append('B'), Document contains `"AB"`.
3rd query: Append('C'), Document contains `"ABC"`.
4th query: UNDO(), Last character is removed, Document contains `"AB"`.
5th query: READ(), Document content will be printed.
6th query: REDO(), Document contains `"ABC"`.
7th query: READ(), Document content will be printed.

---

### Example 2

**Input:**
`arr[] = [[1 'D'], [2], [4]]`

**Output:**
`[""]`

**Explanation:** Queries will be processed as:
1st query: Append('D'), Document contains `"D"`.
2nd query: UNDO(), Last character is removed, Document becomes empty.
3rd query: READ(), Empty Document will be printed.

---

## Constraints

* `1 ≤ q ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(1)`
* **Auxiliary Space:** `O(n)`

---

---

## 2) Text explanation (core idea)

This is the classic **Undo/Redo** design using **two stacks**:

* **document**: current content (we can store as a list of characters)
* **undo_stack**: operations you can undo (or simpler: characters that were appended and not undone)
* **redo_stack**: operations you can redo (characters removed by undo)

### Rules

1. **append(x)**

   * add `x` to document
   * push `x` to `undo_stack` (it’s undoable)
   * **clear `redo_stack`** (because a new edit invalidates redo history)

2. **undo()**

   * if document not empty (or undo_stack not empty):

     * remove last char from document
     * push that char to `redo_stack`

3. **redo()**

   * if redo_stack not empty:

     * pop char from redo_stack
     * append it back to document
     * push it into `undo_stack` again

4. **read()**

   * return `"".join(document)`

**Complexity:** Each op is O(1) except `read()` which is O(n) to build the string (that’s normal).

---

## Step-by-step dry run

Example 1:
`arr = [[1 'A'], [1 'B'], [1 'C'], [2], [4], [3], [4]]`

Start:

* doc = ""
* undo_stack = []
* redo_stack = []

### 1) append('A')

* doc = "A"
* undo_stack = ['A']
* redo_stack = [] (cleared)

### 2) append('B')

* doc = "AB"
* undo_stack = ['A','B']
* redo_stack = []

### 3) append('C')

* doc = "ABC"
* undo_stack = ['A','B','C']
* redo_stack = []

### 4) undo()

* remove last 'C' from doc → doc="AB"
* redo_stack push 'C' → redo_stack=['C']
* undo_stack effectively now last append is undone (we can keep doc as truth)

### 5) read()

* output: "AB"

### 6) redo()

* pop from redo_stack: 'C'
* append back → doc="ABC"
* redo_stack=[]
* undo_stack updated again (conceptually 'C' is active)

### 7) read()

* output: "ABC"

Outputs: `["AB", "ABC"]`

---

## 3) Python codes (easy + interview-expected)

### A) Easy / direct approach (two stacks + document list) ✅ interview-expected

This is the cleanest and most common.

```python
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
```

---

### B) Slightly more “formal” (explicit undo_stack + redo_stack)

Sometimes interviewers like “operations history”. Here, `undo_stack` stores appended chars that are currently active.

```python
class Solution:
    def __init__(self):
        self.document_chars = []
        self.undo_stack = []  # chars that are currently in the document via append/redo
        self.redo_stack = []  # chars removed by undo

    def append(self, x):
        # Time: O(1)
        self.document_chars.append(x)
        self.undo_stack.append(x)

        # Any new append clears redo history
        self.redo_stack.clear()

    def undo(self):
        # Time: O(1)
        if self.undo_stack:
            last_char = self.undo_stack.pop()
            self.document_chars.pop()      # same char removed from end
            self.redo_stack.append(last_char)

    def redo(self):
        # Time: O(1)
        if self.redo_stack:
            ch = self.redo_stack.pop()
            self.document_chars.append(ch)
            self.undo_stack.append(ch)

    def read(self):
        # Time: O(n)
        return "".join(self.document_chars)
```

---

## 4) Interview: how to remember quickly + expected Q&A

### Quick memory hook

**“Two stacks: UNDO pops doc → pushes redo; REDO pops redo → pushes doc. New append clears redo.”**

Mnemonic:

> **“Append clears redo. Undo moves to redo. Redo moves back.”**

---

## Common interviewer questions & answers

### Q1) Why do we need two stacks?

**A:** Undo and redo are opposite directions. Undo removes the latest change and stores it so redo can reapply it. Two stacks naturally represent these two directions.

---

### Q2) Why must append clear the redo stack?

**A:** Because redo is only valid if you haven’t made a new edit after undo. Any new append changes history and invalidates the redo chain.

---

### Q3) What is the time complexity of operations?

**A:** `append/undo/redo` are **O(1)**. `read()` is **O(n)** because converting list to string costs linear time.

---

### Q4) What happens if undo is called on an empty document?

**A:** Do nothing (safe no-op).

---

### Q5) What happens if redo is called with empty redo stack?

**A:** Do nothing.

---

### Q6) How would you support undo/redo for more complex operations (insert, delete range)?

**A:** Store operations as records (type, position, text) in undo_stack; redo_stack stores the inverse operations. This becomes the Command Pattern.

---

---

## 5) Real-world use cases (few, very relatable)

1. **Text editors / IDEs (VSCode, Google Docs):**
   Every keystroke (append) can be undone/redone instantly. Same exact two-stack model.

2. **Form editing / UI state changes (web/app):**
   User changes a setting or toggles options; undo restores the previous state and redo reapplies it (common in design tools, dashboards).

3. **Photo/design tools (Figma/Photoshop-like actions):**
   Actions are stored as reversible commands. Undo/redo stacks track applied vs undone actions.

---

## 6) Full Python program (reads queries, prints READ outputs, times full run)

### Input format supported

* First line: `q` (number of queries)
* Then `q` lines:

  * `1 x` → append character `x`
  * `2` → undo
  * `3` → redo
  * `4` → read (print later)

### Output

* Prints each READ result on a new line (in the order encountered).
* Prints runtime to **stderr** (won’t pollute judged output).

```python
import sys
import time

class Solution:
    def __init__(self):
        # Document stored as list of chars for O(1) append/pop at end
        # Space: O(n) where n = current document size
        self.document_chars = []

        # Redo stack stores characters removed by undo (to restore later)
        # Space: O(n) in worst case
        self.redo_stack = []

    def append(self, x):
        # Append x into document
        # Time: O(1)
        self.document_chars.append(x)

        # New edit invalidates redo history
        # Time: O(r) for clear where r is redo size; overall amortized ok
        self.redo_stack.clear()

    def undo(self):
        # Undo last APPEND: remove last character
        # Time: O(1)
        if self.document_chars:
            removed_char = self.document_chars.pop()
            # Save removed char to redo stack
            self.redo_stack.append(removed_char)

    def redo(self):
        # Redo most recent undone operation
        # Time: O(1)
        if self.redo_stack:
            char_to_restore = self.redo_stack.pop()
            self.document_chars.append(char_to_restore)

    def read(self):
        # Return current content
        # Time: O(n) to join characters into a string
        # Space: O(n) for the created string
        return "".join(self.document_chars)


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        # Demo run if no input is provided
        demo_queries = [(1, 'A'), (1, 'B'), (1, 'C'), (2,), (4,), (3,), (4,)]
        print("Demo Input:")
        print(demo_queries)

        editor = Solution()
        start = time.perf_counter()

        outputs = []
        for q in demo_queries:
            if q[0] == 1:
                editor.append(q[1])
            elif q[0] == 2:
                editor.undo()
            elif q[0] == 3:
                editor.redo()
            else:  # 4
                outputs.append(editor.read())

        end = time.perf_counter()

        print("Demo Output:")
        for out in outputs:
            print(out)
        sys.stderr.write(f"[Runtime] {end - start:.6f} seconds\n")
        return

    # -------------------------
    # Parse input
    # -------------------------
    # Expected:
    # q
    # query lines...
    # Time: O(q)
    # Space: O(q) for tokens already read
    idx = 0
    q = int(data[idx].decode())
    idx += 1

    editor = Solution()
    read_outputs = []

    # -------------------------
    # Execute and time full run
    # -------------------------
    start_time = time.perf_counter()

    # Process queries
    # append/undo/redo: O(1) each
    # read: O(n) each (n = current doc length)
    for _ in range(q):
        operation = int(data[idx].decode())
        idx += 1

        if operation == 1:
            # Query: 1 x
            x = data[idx].decode()
            idx += 1
            editor.append(x)

        elif operation == 2:
            editor.undo()

        elif operation == 3:
            editor.redo()

        else:  # operation == 4
            read_outputs.append(editor.read())

    end_time = time.perf_counter()

    # Print all READ outputs (one per line)
    sys.stdout.write("\n".join(read_outputs) + ("\n" if read_outputs else ""))

    # Print runtime to stderr (keeps stdout clean for OJ)
    sys.stderr.write(f"[Runtime] {end_time - start_time:.6f} seconds\n")


if __name__ == "__main__":
    main()


"""
========================
Sample Input
========================
7
1 A
1 B
1 C
2
4
3
4

Expected Output
AB
ABC

========================
Sample Input
========================
3
1 D
2
4

Expected Output

(prints empty line)
"""
```
