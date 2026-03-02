### ✅ 5-line pseudo-code template (memorize)

```text
i = 0, j = m-1
bestPair = (arr1[i], arr2[j]), bestDiff = abs(sum - x)
while i < n and j >= 0:
    update best if abs(arr1[i] + arr2[j] - x) smaller
    if sum > x: j-- else if sum < x: i++ else return (arr1[i], arr2[j])
return bestPair
```

### 🧠 Easy mnemonic

**“Small + Big, then Nudge”**

* Start **smallest** in arr1 + **biggest** in arr2
* If sum is **too big** → nudge the **big** left (`j--`)
* If sum is **too small** → nudge the **small** right (`i++`)
* Track the best diff as you go

Even shorter: **“SB → compare → move closer”** (Small-Big)

---

### ⏱ 60-second recall script (say this before/inside interview)

1. “Arrays are sorted, so I can do a two-pointer sweep.”
2. “Start with smallest in arr1 and largest in arr2.”
3. “Compute sum, update best using `abs(sum-x)`.”
4. “If sum > x, decrease sum by moving `j` left; if sum < x, increase sum by moving `i` right.”
5. “If sum == x, return immediately.”
6. “Each pointer moves at most once across its array → `O(n+m)` time, `O(1)` space.”
