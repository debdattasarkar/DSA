## ✅ 5-Line Pseudo-Code Template (Memorize This)

```text
freq = {0:1}
px = 0, ans = 0
for each value in arr:
    px ^= value
    ans += freq.get(px ^ k, 0)
    freq[px] += 1
return ans
```

That’s the entire solution skeleton.
You can rebuild it in **any language in under 30 seconds**.

---

# 🧠 Easy Mnemonic

### 🔑 “PX → Need → Count → Store”

* **PX** = update Prefix XOR
* **Need** = px ^ k
* **Count** = add freq[Need]
* **Store** = increment freq[px]

Or even shorter:

### 👉 **“XOR → Need = px^k → Add → Save”**

---

# ⏱ 60-Second Interview Recall Script

When interviewer asks, think through this flow:

1. “This is a prefix XOR problem.”
2. “If subarray XOR = k, then
   prefix[r] ^ prefix[l-1] = k.”
3. “So prefix[l-1] = prefix[r] ^ k.”
4. “That means for every prefix XOR, I just need to know how many times `(currentPrefix ^ k)` appeared before.”
5. “So I’ll maintain a frequency map of prefix XOR values.”
6. “Initialize map with `{0:1}` to handle subarrays starting at index 0.”
7. “Single pass, O(n) time, O(n) space.”

Done. Clean. Confident.

---

# 💡 Why `{0:1}` Is Critical (Quick Mental Check)

If `prefixXor == k` at some index,
then `required = px ^ k = 0`.

We need one occurrence of prefix `0` to count that subarray.
That’s why we initialize:

```text
freq = {0:1}
```

---

# 🎯 One-Line Core Identity to Remember

### **Subarray XOR k → Need previous prefix = px ^ k**

If you remember this one equation:

```
previous_prefix = current_prefix ^ k
```

You can derive everything else.

