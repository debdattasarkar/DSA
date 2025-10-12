**5-line pseudo-code skeleton** + **easy mnemonic** so you can recall and rebuild it instantly in *any language* within 30 seconds.

---

## ⚡ 5-Line Universal Pseudo-code Template

```
1. low ← 0, mid ← 0, high ← n - 1
2. while mid ≤ high:
3.     if arr[mid] == 0: swap(arr[low++], arr[mid++])
4.     elif arr[mid] == 1: mid++
5.     else: swap(arr[mid], arr[high--])
```

✅ **Time:** O(n)
✅ **Space:** O(1)
✅ **In-place & one pass**

---

## 🧠 Mnemonic: **“Low–Mid–High, Swap–Check–Fly”**

Break it into a rhythm:

> **Low, Mid, High — Move or Swap, Don’t Cry!**

Or logically:

> **0 → Left**, **1 → Stay**, **2 → Right**

Just remember the **L–M–H triangle:**

* `low` — boundary for 0s
* `mid` — current explorer
* `high` — boundary for 2s

---

## 🧩 Dry Run in 3 Steps (Mental Picture)

Array: `[2, 0, 1]`
Start: `low=0, mid=0, high=2`

| Step | arr       | low | mid | high | Action                     |
| ---- | --------- | --- | --- | ---- | -------------------------- |
| 1    | [1, 0, 2] | 0   | 0   | 1    | 2→end swap, high--         |
| 2    | [0, 1, 2] | 0   | 0   | 1    | 0→front swap, low++, mid++ |
| 3    | [0, 1, 2] | 1   | 1   | 1    | mid==1 → mid++ stop        |

✅ Sorted `[0,1,2]`

---

## 💡 60-Second Recall Routine (Pre-Interview)

Repeat this mini mantra:

> “Three pointers: Low, Mid, High.
> While Mid ≤ High:
> 0 → swap left,
> 1 → skip,
> 2 → swap right.”

That’s it — you can now rebuild DNF in any syntax.

---

## ⚙️ Rebuild in 4 Languages Instantly

| Language       | 30-sec Rebuild Code                                                                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python**     | `while mid<=high: if arr[mid]==0: arr[low],arr[mid]=arr[mid],arr[low]; low+=1; mid+=1 elif arr[mid]==1: mid+=1 else: arr[mid],arr[high]=arr[high],arr[mid]; high-=1` |
| **C++**        | `while(mid<=high){ if(a[mid]==0) swap(a[low++],a[mid++]); else if(a[mid]==1) mid++; else swap(a[mid],a[high--]); }`                                                  |
| **Java**       | `while(mid<=high){ if(arr[mid]==0){ swap(arr,low++,mid++);} else if(arr[mid]==1) mid++; else swap(arr,mid,high--); }`                                                |
| **JavaScript** | `while(mid<=high){ if(a[mid]==0){ [a[low],a[mid]]=[a[mid],a[low]]; low++; mid++; } else if(a[mid]==1) mid++; else { [a[mid],a[high]]=[a[high],a[mid]]; high--; } }`  |

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

> “Low–Mid–High.
> If 0 → swap left.
> If 1 → move mid.
> If 2 → swap right.
> Keep shrinking the unknown zone.”

Memorize that, and you’ll *never* forget the Dutch National Flag logic under interview stress.
