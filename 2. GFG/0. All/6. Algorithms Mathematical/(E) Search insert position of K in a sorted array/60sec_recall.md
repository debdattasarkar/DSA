## 5-line pseudo-code template (Search Insert Position / Lower Bound)

```text
left = 0, right = n
while left < right:
    mid = (left + right) // 2
    if arr[mid] < k: left = mid + 1
    else: right = mid
return left
```

That returns:

* index of `k` if present, else
* correct insertion index to keep array sorted.

---

## Easy mnemonic (60-second recall)

### Phrase to remember ✅

> **“LOWER BOUND = first >= k.”**

### 3-step recall

1. **Answer is boundary**, not “found/not found”.
2. Maintain **[left, right)** i.e., right is **n**, not n-1.
3. Rule:

   * `arr[mid] < k` → go right (`left = mid + 1`)
   * else → go left (`right = mid`)

### Tiny mental chant

> **“<k move left up, >=k pull right down.”**

If you can say “first index with value ≥ k”, the code basically writes itself.
