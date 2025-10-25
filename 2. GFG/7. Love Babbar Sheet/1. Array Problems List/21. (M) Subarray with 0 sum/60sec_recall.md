**5-line pseudo-code template + 60s recall kit** for
🧩 **Subarray with 0 Sum** (one of the most frequent logic-based array questions).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
sum = 0
seen = {}
for each num in arr:
    sum += num
    if sum == 0 or sum in seen: return True
    seen.add(sum)
return False
```

✅ **O(n)** time, **O(n)** space
✅ Works for both positive & negative numbers
✅ You can rebuild this in **Python, C++, Java, Go, or JS** in 30 seconds.

---

## 🧠 Mnemonic — “**S-A-S-H**” → *Sum, Add, Seen, Hit*

| Step  | Action                             | Quick memory image                 |
| ----- | ---------------------------------- | ---------------------------------- |
| **S** | **Sum** prefix values one by one   | Picture a running total meter      |
| **A** | **Add** current sum to `seen` set  | Dropping each prefix into a bucket |
| **S** | **Seen again?** → subarray = 0-sum | Alarm goes off if prefix repeats   |
| **H** | **Hit zero early?** return True    | 0-sum prefix = valid subarray      |

> 🧩 **Catchphrase:**
> “Keep a running sum; if you see it again — zero lies in between.”

---

## 🕒 60-Second Interview Recall Routine

**Step 1 – Restate problem (5s):**
“Need to detect if any contiguous subarray sums to zero.”

**Step 2 – Key insight (10s):**
“If prefix sums repeat, the numbers between cancel to zero.”

**Step 3 – Visualize loop (15s):**

* `sum += arr[i]`
* If `sum == 0` or `sum` seen before → ✅ return True
* Else add `sum` to set

**Step 4 – Complexity recall (10s):**
Time **O(n)**, Space **O(n)** (hash lookups average O(1)).

**Step 5 – Edge check (20s):**

* Zero element alone? → catches via `sum == 0`.
* All positives? → returns False cleanly.
* Negatives? → still works (prefix diff logic holds).

---

### 🧩 One-line visual cue for memory

> **“Prefix repeats ⇒ zero hides in between.”**
