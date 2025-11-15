**“5-line pseudo-code template” + mnemonic + 60-second recall** for **Max Rectangle in Binary Matrix** — super compact, easy to memorize, usable in ANY language.

---

# ✅ **5-Line Pseudo-Code (Max Rectangle in Binary Matrix)**

*(Optimal O(n·m) solution)*

```
heights = [0]*m
for each row r:
    update heights[c] = heights[c]+1 if mat[r][c]==1 else 0
    area = largestRectangleInHistogram(heights)
    best = max(best, area)
return best
```

And the **largestRectangleInHistogram** (LC84) is also a 5-liner:

```
stack = []
for i in 0..m:
    while stack not empty and h[stack.top] > h[i]:
        compute area with popped height
    push i
return max_area
```

---

# 🎯 **The Mnemonic: “Build → Histogram → Solve → Repeat → Max”**

Say it like a rhythm:

### **“Row → Heights → Histogram → Max → Next.”**

Or more visually:

🧱 **Row** →
📊 **Heights grow** →
📐 **Histogram rectangle** →
🏆 **Update max** →
➡️ **Next row**

---

# 🧠 **60-Second Interview Recall (What to say)**

### **0–10 sec — Recognize the pattern**

“This is the classic 2D → 1D reduction problem.
We build histograms row by row.”

### **10–20 sec — Explain histogram build**

“For each column c, heights[c] is the number of consecutive 1s upward.”

### **20–35 sec — Core step**

“For each row’s histogram, run Largest Rectangle in Histogram (LRH) using a monotonic stack.”

### **35–45 sec — Complexity**

“Updating heights = O(m), LRH = O(m).
Do this for n rows → **O(n·m)** time, **O(m)** space.”

### **45–55 sec — Why it’s correct**

“Any maximal rectangle ends at some row.
So taking LRH at each row catches all possibilities.”

### **55–60 sec — Implementation summary**

“I keep heights array, update each row, apply LRH, track global max.”

---

# 📌 **Ultra-Compact Version to Remember**

```
for each row:
    grow heights
    best = max(best, LRH(heights))
return best
```

This is *literally all you need* to reconstruct the full solution during an interview.

---

If you want, I can also create a:

📌 **Sticky-note style sketch-note**
📌 **Hand-drawn infographic**
📌 **Color-coded cheat-sheet version**

Just tell me — I can generate it!
