### 5-line pseudo-code template (memorize)

```
five=0; ten=0
for x in arr:
  if x==5: five++
  elif x==10: if five==0: return false; five--; ten++
  else: if ten>0 and five>0: ten--; five--; elif five>=3: five-=3; else: return false
return true
```

---

## Mnemonic (30-sec)

**“10 needs 5. 20 needs 15 → prefer 10+5, else 5+5+5.”**
(or **“SAVE the 5’s: use 10+5 first.”**)

---

## 60-second recall script (what to say in interview)

1. “Ticket costs 5; people pay 5/10/20 in order.”
2. “Track only count of 5s and 10s (20s are never useful as change).”
3. “For 10, must have a 5 to return.”
4. “For 20, need 15: greedily give 10+5 if possible, else 5+5+5.”
5. “Single pass → O(n) time, O(1) space.”
