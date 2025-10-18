**“60-second recall kit”** and **5-line pseudo-code skeleton** for the **Rotate Array by One (Clockwise)** problem — the version you can rebuild in *any* language almost from memory.

---

## 🧠 5-Line Pseudo-code Template (universal skeleton)

```
function rotateRightByOne(arr):
    last = arr[n-1]                  # save last element
    for i from n-1 down to 1:        # move each element one step right
        arr[i] = arr[i-1]
    arr[0] = last                    # put saved element at front
    return arr
```

✅ Works in Python, C++, Java, JavaScript — identical logic, different syntax only.

---

## 🧩 Mnemonic to Remember It

> **“Save → Shift → Place → Return.”**

1️⃣ **Save** the last element.
2️⃣ **Shift** others right (go backwards so you don’t overwrite).
3️⃣ **Place** the saved element at the front.
4️⃣ **Return** or print the rotated array.

Say to yourself:

> “Save → Shift → Place → Return.”

That’s your mental trigger for the 4 operations.

---

## ⚙️ Quick Example (mental dry run)

```
arr = [1, 2, 3, 4, 5]
```

* Save last = 5
* i=4→1: shift right ⇒ `[1,1,2,3,4]`
* Place last at arr[0] ⇒ `[5,1,2,3,4]` ✅

Edge cases: empty or length-1 → unchanged.

---

## ⏱️ 60-Second Pre-Interview Recall

When interviewer says:

> “Rotate an array clockwise by one.”

You instantly think:

1️⃣ “I’ll save the last element.”
2️⃣ “Walk backward shifting each to the right.”
3️⃣ “Drop the saved one at front.”
4️⃣ “O(n) time, O(1) space.”

Optional follow-up:

> “If asked for rotate by *k*, I’ll use the 3-reverse trick.”

---

## 🧠 10-Second “Why” Explanation

> “Scanning backwards prevents overwriting; every element moves once,
> so time O(n) and only one temporary variable — O(1) space.”

---

## ✅ Quick Recall Table

| Step | Action                           | Purpose           | Keyword    |
| ---- | -------------------------------- | ----------------- | ---------- |
| 1    | Save last element                | Don’t lose it     | **Save**   |
| 2    | Shift elements right (backwards) | Make room         | **Shift**  |
| 3    | Place saved element at index 0   | Complete rotation | **Place**  |
| 4    | Return / print                   | Deliver result    | **Return** |

🧩 **Mnemonic:** **S-S-P-R → “Save, Shift, Place, Return.”**

---

Memorize **these four verbs**, and you can rebuild the entire algorithm in under **30 seconds** in *any language* during an interview.
