## 5-line pseudo-code template (k queues in one array)

```text
init: front[k]=rear[k]=-1; next[i]=i+1; next[n-1]=-1; free=0
enqueue(x,i): if free==-1 return; idx=free; free=next[idx]; data[idx]=x; next[idx]=-1; attach idx to (front/rear) of queue i
dequeue(i): if front[i]==-1 return -1; idx=front[i]; front[i]=next[idx]; if front[i]==-1 rear[i]=-1; next[idx]=free; free=idx; return data[idx]
isEmpty(i): return front[i]==-1
isFull(): return free==-1
```

### Mnemonic (easy to recall)

**“FRONT/REAR + NEXT + FREE”**

* Every queue has **Front/Rear**
* Every slot has **Next** pointer
* One **Free** pointer manages empty slots

Or even shorter: **“Take from FREE, link by NEXT, track FRONT/REAR.”**

---

## 60-second recall (what to say + do)

1. **Problem hook (10s):**
   “Need k queues in one array without wasting space → use a free-list.”

2. **Data structures (10s):**
   “Maintain `data[n]`, `next[n]`, `front[k]`, `rear[k]`, and `free` head.”

3. **How free list works (10s):**
   “`free` points to first free index; `next[]` links free slots like 0→1→2→….”

4. **Enqueue in O(1) (15s):**
   “Pop an index from `free`, write value, set next=-1, append to queue via `rear`.”

5. **Dequeue in O(1) (15s):**
   “Remove `front`, move front forward, if empty set rear=-1, push removed index back to free.”

That’s the whole thing—you can rebuild the code from those five steps quickly.
