### 5-line pseudo-code template (memorize)

```
stack = empty
for ch in s:
  if ch != ')': push ch
  else:
    seenOp = false; pop until '('; if operator found → seenOp = true
    pop '('; if not seenOp → return true
return false
```

---

## Easy mnemonic (30 seconds)

**“NO OP inside brackets ⇒ REDUNDANT.”**
(or **“Close bracket → check operator → none? useless.”**)

---

## 60-second interview recall script

1. “Redundant brackets are those that don’t change expression meaning.”
2. “Parentheses are useful only if there is an operator inside them.”
3. “Scan with a stack; on encountering `)`, inspect contents until `(`.”
4. “If no operator found, return true immediately.”
5. “Otherwise continue. Linear time, linear space.”

You can rebuild the entire solution from this in **any language in under 30 seconds**.
