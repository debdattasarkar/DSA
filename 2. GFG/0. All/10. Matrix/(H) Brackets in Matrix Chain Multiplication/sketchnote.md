Here’s a “draw-it-yourself” sketch note you can copy to paper/tablet. I’ll mark **colors + icons** so you can color them in quickly.

---

## Overall Layout

Use **landscape** orientation.
Put this **in the center**, everything else radiates out.

```text
[YELLOW STICKY]  🪟 SLIDING WINDOW
----------------------------------
"Expand → Shrink → Save"
(O(n) time, O(1) extra space)
```

Now we add 3 colored branches: **GROW (green), FIX (red), RECORD (blue)**.

---

## 1️⃣ Left: GROW (expand window)

Draw an arrow from the center to the **left**:

```text
[GREEN STICKY]  💚 GROW  (move RIGHT)
-------------------------------------
end++               ← pointer moves right
add A[end]          ← include new element in window_state
```

Under it, small diagram:

```text
Array:
[ a0  a1  a2  a3  a4  a5 ]
        [--------]
       start    end →

Caption (in green):  
"GROW = **include more** (extend right side)"
```

---

## 2️⃣ Top: FIX (shrink window)

Arrow from center **up**:

```text
[RED STICKY]  ❤️ FIX  (while RULE broken)
----------------------------------------
while window_invalid():
    remove A[start]     ← element leaves window
    start++             ← move left pointer
```

Next to it, write the word **RULE** in a red cloud and list examples:

```text
RULE examples:
- size > k ?
- sum > target ?
- duplicate char ?
```

Tiny picture:

```text
[ a0  a1  a2  a3  a4  a5 ]
      [------]
   start →   end
(shrink from the left)
```

Caption (in red):
"FIX = **trim the left** till rule OK"

---

## 3️⃣ Right: RECORD (save answer)

Arrow from center **right**:

```text
[BLUE STICKY]  💙 RECORD  (best answer)
---------------------------------------
best = update(best, window_state)
   e.g. max / min / longest_length
```

Draw a **blue trophy 🏆** labeled:

```text
🏆 best_so_far
```

Caption (blue):
"RECORD = **trophy update**"

---

## 4️⃣ Bottom: 5-line Template (the code you recall)

Make a long **orange sticky** at the bottom:

```text
[ORANGE STRIP]  🧠 5-LINE TEMPLATE
----------------------------------
1. start = 0; best = INIT; window_state = EMPTY
2. for end in [0 .. n-1]:
3.     add A[end] to window_state        # 💚 GROW
4.     while window_is_invalid():        # ❤️ FIX
           remove A[start]; start += 1
5.     best = update(best, window_state) # 💙 RECORD
```

Underneath, write the **mnemonic** in big letters:

```text
GROW → FIX → RECORD
(Expand → Shrink → Save)
```

Maybe draw 3 small arrows:

* 🟩 Green arrow labeled **GROW**
* 🟥 Red arrow labeled **FIX**
* 🟦 Blue arrow labeled **RECORD**

---

## 5️⃣ Side Sticky: Example (Max Sum of Size k)

Add a small **purple sticky** in one corner:

```text
[PURPLE] Example: Max Sum Size k
--------------------------------
window_state = sum
window_invalid() = size > k
RECORD: best = max(best, sum) when size == k
```

Optional second tiny note for strings (longest substring w/o repeats):

```text
window_state = char counts
invalid = any count > 1
RECORD = max(best, window_length)
```

---

## How to Use This

1. Before the interview, **redraw this page once** (takes ~2 minutes).
2. Say out loud:

   * “**GROW → FIX → RECORD**”
   * “Expand, while-bad shrink, then update answer.”
3. During the interview, rebuild code from the 5-line orange strip in any language.

If you'd like, I can next turn this into a small PDF-like ASCII page you can print and color in.
