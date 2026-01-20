### 5-line pseudo-code template (memorize)

```
stack = empty
for digit in s:
    while k>0 and stack not empty and stack.top > digit: pop; k--
    push digit
if k>0: remove last k digits from stack
ans = stripLeadingZeros(join(stack)); return ans if ans != "" else "0"
```

---

## Easy mnemonic (super quick)

**“Pop-Big, Push-New, Trim-End, Strip-0”**

* **Pop-Big**: while top > current and k>0
* **Push-New**: push current digit
* **Trim-End**: if k remains, cut from end
* **Strip-0**: remove leading zeros, empty ⇒ `"0"`

---

## 60-second recall script (what to rehearse)

1. “Goal: smallest number after removing exactly k digits, order preserved.”
2. “Greedy: if a smaller digit appears, delete bigger digits before it (most impact on left).”
3. “So keep digits in a **monotonic increasing stack**.”
4. “Scan left→right: while k>0 and top>current → pop, k--. Then push.”
5. “If k still left, remove from end.”
6. “Strip leading zeros.”
7. “If empty, return 0.”