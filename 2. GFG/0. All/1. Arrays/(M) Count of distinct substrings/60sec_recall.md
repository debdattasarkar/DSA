Here’s a tiny “cheat card” you can keep in your head.

---

## 5-Line Pseudo-Code (Trie version)

```text
root = new TrieNode(); ans = 0
for i in 0..n-1:
    node = root
    for j in i..n-1:
        c = s[j]
        if c not in node.children: node.children[c] = new TrieNode(); ans++
        node = node.children[c]
return ans
```

That’s the whole algorithm in 5 lines. From this you can rebuild full code in any language.

---

## Easy Mnemonic (60-second recall)

Think: **“Start → Walk → Check → Create → Count”**

1. **Start** at each index `i` in the string.
2. **Walk** forward (inner loop over `j`).
3. **Check** if edge for character `c = s[j]` exists from current node.
4. If not, **Create** a child node.
5. Every newly created node, **Count** it as a new distinct substring.

Repeat that phrase to yourself before the interview:

> “For each start, walk forward; if edge missing, create node and count it.”

…and the 5-line pseudo-code will pop back into your head.
