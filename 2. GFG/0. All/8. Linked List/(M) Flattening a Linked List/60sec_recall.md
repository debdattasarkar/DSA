### 5-line pseudo-code template (memorize)

```
flatten(node):
    if node == null or node.next == null: return node
    right = flatten(node.next)
    node.next = null
    return mergeBottom(node, right)     // merge two sorted bottom-lists
```

*(And `mergeBottom(a,b)` is the standard sorted-merge using `bottom` pointers.)*

---

## Mnemonic (30-sec)

**“RIGHT → MERGE”**
Flatten the **RIGHT** side first, then **MERGE** two sorted bottom lists.

---

## 60-second recall script (what to say in interview)

1. “Each column is a sorted list via `bottom`, and `next` links the heads—this is merge-k-sorted-lists.”
2. “I’ll flatten from the right: base case 0/1 head.”
3. “Flatten `root.next` to get one sorted bottom chain.”
4. “Merge current column with that chain using standard two-list merge (on `bottom`).”
5. “Set `next=None` while merging. Result is fully sorted using only `bottom` pointers.”
