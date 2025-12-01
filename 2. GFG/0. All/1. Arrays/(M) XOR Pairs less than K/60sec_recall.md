
---

## 5-Line Pseudo-Code (core idea)

```text
root = emptyTrie(); ans = 0
for each x in arr:
    ans += countLess(root, x, k)        // #previous y with x^y < k
    insert(root, x)                     // add x for future pairs
return ans
```

And inside `countLess` you just need the **bit rule**:

```text
for bit from MSB..LSB:
    bx = bit(x); bk = bit(k)
    if bk == 1: add subtree(node, bx); node = child(node, 1-bx)
    else:       node = child(node, bx)
```

That’s it—those 5 “effective” lines are enough to rebuild the full solution.

---

## 60-Second Mnemonic

Remember this phrase:

> **“Past-Trie, Query-then-Insert; when k-bit = 1, add same-bit branch and go opposite.”**

Break it down:

1. **Past-Trie** – keep a bitwise trie of all previous numbers.
2. **Query-then-Insert** – for each `x`, first count pairs with earlier numbers, then insert `x`.
3. **When k-bit = 0** – XOR bit must be 0 → follow **same bit** as `x`.
4. **When k-bit = 1** –

   * **Add same-bit branch** (XOR bit 0 ⇒ already `< k`),
   * **Go opposite** bit branch (XOR bit 1 ⇒ still equal to `k`, keep checking).

If you can replay:

> “Trie of past numbers, for each x: query-then-insert; k-bit 0 → same; k-bit 1 → add same, go opposite,”

you’ll be able to reconstruct both the logic and the code in any language very quickly.
