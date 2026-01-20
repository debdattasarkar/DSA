### 5-line pseudo-code template (memorize)

```
doc = empty list/stack, redo = empty stack
append(x): doc.push(x); redo.clear()
undo(): if doc not empty: redo.push(doc.pop())
redo(): if redo not empty: doc.push(redo.pop())
read(): return join(doc)
```

That’s the whole logic.

---

## Easy mnemonic (fast recall)

**“A-U-R-R”**

* **A**ppend → push to doc, **clear redo**
* **U**ndo → pop doc, push to redo
* **R**edo → pop redo, push to doc
* **R**ead → join doc

Or even shorter phrase:

> **“Undo moves → redo stack, Redo moves ← back. Append resets redo.”**

---

## 60-second recall script (what to mentally rehearse)

1. “We need undo/redo for append-only edits.”
2. “Use **two stacks**: `doc` (current text) and `redo` (undone chars).”
3. “Append: push to doc; **clear redo** (new branch).”
4. “Undo: if doc not empty, pop last char and push to redo.”
5. “Redo: if redo not empty, pop and push back to doc.”
6. “Read: join doc into string.”
7. “Complexities: append/undo/redo O(1); read O(n).”
