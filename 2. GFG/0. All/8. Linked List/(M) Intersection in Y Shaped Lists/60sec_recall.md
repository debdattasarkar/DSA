### 5-line pseudo-code template (memorize)

```
p1 = head1; p2 = head2
while p1 != p2:
    p1 = (p1.next if p1 else head2)
    p2 = (p2.next if p2 else head1)
return p1    // intersection node
```

---

## Mnemonic (30-sec)

**“SWITCH → SAME distance → MEET”**
(aka “Two runners swap tracks and meet at merge.”)

---

## 60-second recall script (say this in interview)

1. “Intersection means **same node reference**, not same value.”
2. “Use two pointers from both heads.”
3. “Move one step each; when one hits null, **switch it** to the other head.”
4. “Both will traverse `len1+len2`, so length difference cancels and they **meet at intersection**.”
5. “Return that node. Complexity: `O(n+m)` time, `O(1)` space.”
