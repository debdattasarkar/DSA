**Core 5-line skeleton**, an **easy mnemonic**, and a **60-second recall routine**.

---

## ⚡ The 5-Line Universal Pseudo-code (for Kth Smallest via Quickselect)

```
1.  choose pivot ← random element
2.  partition arr into L (<pivot), E (=pivot), R (>pivot)
3.  if k ≤ len(L):      recurse on L
4.  elif k ≤ len(L)+len(E): return pivot
5.  else:               recurse on R with k - len(L) - len(E)
```

---

### 🧠 Mnemonic — “**P–P–C–E–R**” (Pivot–Partition–Check–Equal–Recurse)

> **Say aloud:** “Pick pivot, Partition, Check left size, Equal → pivot, else Recurse right.”

That’s literally the whole algorithm.
Everything in Python, C++, or Java can be rebuilt from this skeleton in 30 seconds.

---

### 🧩 Example mental dry run

`arr = [7,10,4,3,20,15], k=3`
Pivot = 7
Partition → `L=[4,3], E=[7], R=[10,20,15]`
`len(L)=2`, `len(L)+len(E)=3` → `k=3` ⇒ ✅ return `pivot=7`

---

### 🧠 60-Second Recall Routine (Pre-Interview Recap)

Say this out loud (or mentally) right before your interview:

> “Pick a pivot. Partition into smaller, equal, greater.
> If k is in left → recurse left.
> If k lands in equal → return pivot.
> Else recurse right adjusting k.”

Done — you’ve rebuilt Quickselect.

---

## 💪 Quick Code Reconstruction (in 4 languages)

| Language   | 5-line rebuild                                                                                                                                                                                                                    |                                                                                                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python** | `pivot=random.choice(arr); L=[x for x in arr if x<pivot]; E=[x for x in arr if x==pivot]; R=[x for x in arr if x>pivot]; if k<=len(L): return kth(L,k); elif k<=len(L)+len(E): return pivot; else: return kth(R,k-len(L)-len(E))` |                                                                                                                                                                                                         |
| **C++**    | `pivot=a[rand()%n]; partition; if(k<=L.size()) recurse L; else if(k<=L.size()+E.size()) return pivot; else recurse R with k-...`                                                                                                  |                                                                                                                                                                                                         |
| **Java**   | `pivot=arr[random]; partition; if(k<=leftCount) recurse left; else if(k<=leftCount+equalCount) return pivot; else recurse right.`                                                                                                 |                                                                                                                                                                                                         |
| **JS**     | `pivot=arr[Math.random()*arr.length                                                                                                                                                                                               | 0]; let L=arr.filter(x=>x<pivot),E=arr.filter(x=>x===pivot),R=arr.filter(x=>x>pivot); if(k<=L.length)return kth(L,k);else if(k<=L.length+E.length)return pivot;else return kth(R,k-L.length-E.length);` |

---

## 💡 Pattern Extension (Reuses the same skeleton)

You can reuse this **exact 5-line skeleton** for:

* **Kth largest** → just flip inequalities (`>`/`<`)
* **Median of array**
* **Find percentile (P90, P95, etc.)**
* **Order statistics in streaming data**
* **Partition-based QuickSort**

---

✅ **Final 60-sec summary mantra:**

> “Pivot → Partition → Check Left → Equal → Recurse Right.”
> (That’s P–P–C–E–R — the Quickselect heartbeat.)

If you say that sequence in your head before an interview, you’ll never blank out — it’ll instantly reconstruct the entire Kth Smallest logic in any language.
