
---

# ⚖️ Difference Between “Minimize the Heights I” and “Minimize the Heights II”

| 🔢 Aspect                     | **Minimize the Heights I**                                                         | **Minimize the Heights II**                                             |
| ----------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Problem version**           | Easier / base version                                                              | Modified / constrained version                                          |
| **Operation rule**            | Each tower **may** be increased or decreased by `k` (choice is optional per tower) | Each tower **must** be either increased **or** decreased by exactly `k` |
| **Negative heights allowed?** | ✅ **Yes**, heights can go negative                                                 | ❌ **No**, result must have **non-negative** heights                     |
| **When can we skip a tower?** | Implicitly, we can choose not to change some tower (by deciding same +k and -k)    | No skipping — all towers must be modified                               |
| **Typical line in code**      | `for i in range(1, n):` → no restriction on negative                               | `if arr[i] - k < 0: continue` → skip splits that cause negatives        |
| **Example effect**            | More flexible; fewer constraints → potentially smaller difference                  | Slightly larger difference because of mandatory modifications           |
| **Used in interviews for**    | Understanding greedy logic, baseline pattern                                       | Edge constraints + careful handling of non-negativity                   |
| **Company tags**              | Adobe                                                                              | Microsoft, Adobe                                                        |
| **Accuracy (on GFG)**         | ~26% (easier)                                                                      | ~15% (stricter, more pitfalls)                                          |

---

### 💡 Intuitive difference:

Think of it as two policies applied to a factory of towers:

| Version        | Analogy                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------- |
| **Heights I**  | “You can adjust towers freely by ±k (some you can even skip).”                              |
| **Heights II** | “Every tower must be adjusted exactly once by ±k, and heights can’t go below ground level.” |

---

## 🧩 Example illustration

**Input:** `arr = [1, 5, 8, 10], k = 2`

| Case       | Allowed Negatives? | Modified Array                                                  | Output Difference |
| ---------- | ------------------ | --------------------------------------------------------------- | ----------------- |
| Heights I  | ✅ Yes              | `[3, 3, 6, 8]`                                                  | `8 - 3 = 5`       |
| Heights II | ❌ No               | `[1+2, 5-2, 8-2, 10-2] → [3, 3, 6, 8]` (valid here, still same) | `5`               |

**Input:** `arr = [1, 10, 14, 14, 14, 15], k = 6`

| Case       | Negative check                                      | Result                                       |
| ---------- | --------------------------------------------------- | -------------------------------------------- |
| Heights I  | Allowed → we can even do `1 - 6 = -5`               | Smaller possible diff (since negatives okay) |
| Heights II | Not allowed (`1 - 6` invalid), must skip such cases | Slightly larger final diff                   |

---

## 🔁 Core code difference

### Heights I

```python
for i in range(1, n):
    small = min(arr[0] + k, arr[i] - k)
    big   = max(arr[i-1] + k, arr[-1] - k)
    ans   = min(ans, big - small)
```

### Heights II

```python
for i in range(1, n):
    if arr[i] - k < 0:    # ensure non-negative tower
        continue
    small = min(arr[0] + k, arr[i] - k)
    big   = max(arr[i-1] + k, arr[-1] - k)
    ans   = min(ans, big - small)
```

---

## 🧠 Interview recall line

> “The only difference between *Heights I* and *II* is that in version II, every tower must be changed exactly once, and no tower can go below zero — so you add an extra `if arr[i] - k < 0: continue` check.”

---

✅ **Summary Table (to memorize quickly):**

| Keyword              | Heights I | Heights II                    |
| -------------------- | --------- | ----------------------------- |
| **Negatives**        | Allowed   | Not allowed                   |
| **Mandatory change** | No        | Yes                           |
| **Skip check**       | No need   | `if arr[i] - k < 0: continue` |
| **Flexibility**      | Higher    | Lower                         |
| **Result range**     | Smaller   | Slightly larger               |

---

