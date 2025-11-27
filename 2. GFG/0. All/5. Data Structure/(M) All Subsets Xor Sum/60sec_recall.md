Got it — let’s make a tiny “interview card” for **All Subsets XOR Sum** 🚀

We’ll do:

* 5-line pseudo-code
* Simple mnemonic
* 60-second recall script

---

## ✅ 5-Line Pseudo-Code Template

This is the optimized formula solution:

```text
or_all = 0
for each value in arr:
    or_all = or_all OR value
factor = 1 << (n - 1)          # n = len(arr)
return or_all * factor
```

That’s literally the whole algorithm.

---

## 🎯 Easy Mnemonic

**“OR then Shift”**

1. **OR** all elements → `or_all`
2. **Shift**: multiply by `2^(n-1)` → `or_all << (n-1)`

Or remember the formula:

> **“Subset XOR sum = OR × 2^(n−1)”**

Write it in your notes as:

```text
ans = (a0 | a1 | ... | an-1) << (n-1)
```

---

## ⏱ 60-Second Recall Script (say this before interview)

> “For all subsets, instead of enumerating them, I think bitwise.
> Each bit position acts independently under XOR.
> A bit that never appears in any element contributes nothing.
> A bit that appears in at least one element is 1 in exactly half of all subset XORs, i.e., in 2^(n−1) subsets.
> So the total sum is:
> (bitwise OR of all elements) × 2^(n−1).
> Implementation: compute OR in O(n), then shift left by (n−1).
> Time O(n), space O(1).”

You can literally recite that and then write the 5 lines.
