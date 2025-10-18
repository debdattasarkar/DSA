**5-line pseudo-code skeleton** + **easy mnemonic** so you can recall and rebuild it instantly in *any language* within 30 seconds.

---

## ⚡ 5-Line Universal Pseudo-code Template

```
1. left ← 0, mid ← 0, right ← n - 1
2. while mid ≤ right:
3.     if arr[mid] == 0: swap(arr[left++], arr[mid++])
4.     elif arr[mid] == 1: mid++
5.     else: swap(arr[mid], arr[right--])
```

✅ **Time:** O(n)
✅ **Space:** O(1)
✅ **In-place & one pass**

---

## 🧠 Mnemonic: **“Left–Mid–Right, Swap–Check–Fly”**

Break it into a rhythm:

> **Left, Mid, Right — Move or Swap, Don’t Cry!**

Or logically:

> **0 → Left**, **1 → Stay**, **2 → Right**

Just remember the **L–M–H triangle:**

* `left` — boundary for 0s
* `mid` — current explorer
* `right` — boundary for 2s

---

## 🧩 Dry Run in 3 Steps (Mental Picture)

Array: `[2, 0, 1]`
Start: `left=0, mid=0, right=2`

| Step | arr       | left | mid | right | Action                     |
| ---- | --------- | --- | --- | ---- | -------------------------- |
| 1    | [1, 0, 2] | 0   | 0   | 1    | 2→end swap, right--         |
| 2    | [0, 1, 2] | 0   | 0   | 1    | 0→front swap, left++, mid++ |
| 3    | [0, 1, 2] | 1   | 1   | 1    | mid==1 → mid++ stop        |

✅ Sorted `[0,1,2]`

---

## 💡 60-Second Recall Routine (Pre-Interview)

Repeat this mini mantra:

> “Three pointers: Left, Mid, Right.
> While Mid ≤ Right:
> 0 → swap left,
> 1 → skip,
> 2 → swap right.”

That’s it — you can now rebuild DNF in any syntax.

---

## ⚙️ Rebuild in 4 Languages Instantly

| Language       | 30-sec Rebuild Code                                                                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python**     | `while mid<=right: if arr[mid]==0: arr[left],arr[mid]=arr[mid],arr[left]; left+=1; mid+=1 elif arr[mid]==1: mid+=1 else: arr[mid],arr[right]=arr[right],arr[mid]; right-=1` |
| **C++**        | `while(mid<=right){ if(a[mid]==0) swap(a[left++],a[mid++]); else if(a[mid]==1) mid++; else swap(a[mid],a[right--]); }`                                                  |
| **Java**       | `while(mid<=right){ if(arr[mid]==0){ swap(arr,left++,mid++);} else if(arr[mid]==1) mid++; else swap(arr,mid,right--); }`                                                |
| **JavaScript** | `while(mid<=right){ if(a[mid]==0){ [a[left],a[mid]]=[a[mid],a[left]]; left++; mid++; } else if(a[mid]==1) mid++; else { [a[mid],a[right]]=[a[right],a[mid]]; right--; } }`  |

---

## 🧭 Pattern Link — When This 5-Line Skeleton Appears Again

The same template appears in:

* **Partition algorithms (QuickSort)**
* **3-way partition problems**
* **Segregate negatives/positives**
* **Color sorting or categorical grouping**
* **Stable in-place reordering problems**

---

✅ **Final 60-second summary mantra before interviews:**

> “Left–Mid–Right.
> If 0 → swap left.
> If 1 → move mid.
> If 2 → swap right.
> Keep shrinking the unknown zone.”

Memorize that, and you’ll *never* forget the Dutch National Flag logic under interview stress.
