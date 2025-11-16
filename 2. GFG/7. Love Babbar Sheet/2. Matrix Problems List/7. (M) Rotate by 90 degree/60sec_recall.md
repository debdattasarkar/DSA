Here is the **cleanest, interview-ready “5-line pseudo-code template”**, plus a mnemonic and a 60-second recall routine for the **Rotate Matrix by 90° Clockwise (In-Place)** problem.

---

# ✅ **5-Line Pseudo-Code Template (Rotate 90° Clockwise, In-Place)**

```
for i = 0..n-1:
    for j = i+1..n-1:
        swap(mat[i][j], mat[j][i])      # transpose

for i = 0..n-1:
    reverse(mat[i])                     # reverse each row

return mat
```

That’s it — this is the exact skeleton you can rebuild in any language (Python/C++/Java).

---

# 🎯 **Super-Easy Mnemonic:**

## **“Flip over diagonal → Flip each row.”**

or

## **“Transpose → Reverse Row = Rotate Clockwise.”**

Say it like a chant before coding.

---

# 🧠 **Why it works (10-second explanation)**

* Transpose: **(r, c) → (c, r)**
* Reverse row: **(c, r) → (c, n-1-r)**
  Combined: **(r, c) → (c, n-1-r)** → which is a 90° clockwise rotation.

---

# ⏱ **60-Second Interview Recall (What to say + What to code)**

### **0–10 sec — Recognize the trick**

“Rotate 90° clockwise → transpose + reverse rows.”

### **10–20 sec — Describe verbally**

“Transpose swaps across diagonal. Then reversing rows completes the rotation.”

### **20–30 sec — Write the core code**

```
for i in 0..n-1:
  for j in i+1..n-1:
    swap(a[i][j], a[j][i])

for each row:
  reverse(row)
```

### **30–45 sec — State complexity**

* Time = **O(n²)**
* Extra space = **O(1)** (in-place)

### **45–55 sec — Edge cases**

* n = 1 → unchanged
* Matrix is square only (given by constraints)

### **55–60 sec — Close with intuition**

“Transpose rearranges axes; reversing rows fixes orientation. Fastest and cleanest in-place rotation.”

---

# 📌 **Ultra-Compact Memory Hook**

## **“Diagonal Flip → Row Flip → Done.”**

Keep this sentence in your mind. You’ll never forget the logic again.

---

If you want, I can also generate a **colorful sticky-note sketchnote** for this exact problem (like the earlier ones).
