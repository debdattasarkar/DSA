**5-line universal pseudo-code skeleton** helps you instantly rebuild the full logic in any language (Python, C++, Java, JS, etc.) during an interview.

---

## ⚡ 5-Line Universal Template (Memorize This)

```
1.  left  ← 0
2.  right ← n - 1
3.  while left < right:
4.      swap(arr[left], arr[right])
5.      left++, right--
```

✅ **Mnemonic:**
👉 **"L–R–Swap–Move"**

**Breakdown:**

* **L** → set **Left = 0**
* **R** → set **Right = n-1**
* **Swap** → exchange arr[left] & arr[right]
* **Move** → move pointers toward center (left++, right--)

---

## 💭 60-Second Recall Routine (before interview)

Repeat this aloud or on paper to rebuild code in any language:

> “Left zero, right end, while left smaller, swap and move.”

Then just fill in syntax:

| Language       | 5-line rebuild                                                   |
| -------------- | ---------------------------------------------------------------- |
| **Python**     | `while l < r: arr[l], arr[r] = arr[r], arr[l]; l+=1; r-=1`       |
| **C++**        | `while(l<r) swap(arr[l++], arr[r--]);`                           |
| **Java**       | `while(l<r){ int t=arr[l]; arr[l]=arr[r]; arr[r]=t; l++; r--; }` |
| **JavaScript** | `while(l<r){ [arr[l],arr[r]]=[arr[r],arr[l]]; l++; r--; }`       |

---

## 🧠 Bonus Mental Hook

Imagine two runners starting from both ends of a track (array).
Each step they swap flags (elements) and move inward until they meet.

> “🏁 🏇🏻 Left and right players race toward the middle — swapping flags without fiddle.”

That image sticks **and** captures the exact pointer logic.

---

## 🏆 Use it Anywhere

This **L–R–Swap–Move** pattern appears in:

* Array reversal
* String reversal
* Palindrome check
* Sorting partition (QuickSort)
* Two-sum style problems