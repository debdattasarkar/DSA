
---

# ⭐ **5‑Line Pseudo‑Code Template (Universal, Language‑Agnostic)**

This is the skeleton you can recreate in **30 seconds** in any language:

```
1. Initialize nextSmaller[] = n and empty stack
2. Loop i from n-1 to 0:
3.     While stack not empty AND arr[stack.top] >= arr[i]: pop
4.     If stack not empty: nextSmaller[i] = stack.top
       Push i onto stack
5. Answer = sum(nextSmaller[i] - i for all i)
```

That’s it.  
This is the entire O(n) solution compressed into 5 lines.

---

# ⭐ **60‑Second Recall Mnemonic**

Use this phrase:

### **“Scan from right, pop bigger, next smaller gives range.”**

Breakdown:

- **Scan from right** → You remember to iterate backwards  
- **Pop bigger** → You remember the monotonic stack rule  
- **Next smaller** → You remember what you’re computing  
- **Gives range** → You remember the formula: `NSE[i] - i`

This single sentence reconstructs the entire algorithm.

---

# ⭐ **Ultra‑Short Mental Model (Interview‑Ready)**

### **“How far can I go before someone smaller stops me?”**

That’s literally the problem.

- First element must stay minimum  
- So you extend until a smaller element appears  
- That’s exactly what **Next Smaller Element** gives you  

Once you say this out loud, interviewers know you understand the pattern.

---

# ⭐ **30‑Second Rebuild Strategy (Before Interview Starts)**

When you sit down, mentally rehearse:

1. **Monotonic stack → Next Smaller Element**  
2. **Traverse from right**  
3. **Pop ≥ current**  
4. **Store next smaller index**  
5. **Sum distances**

This is enough to reconstruct the full code.

---
