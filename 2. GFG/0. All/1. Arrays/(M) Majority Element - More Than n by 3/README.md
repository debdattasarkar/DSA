
---

# Majority Element - More Than n/3

**Difficulty:** Medium
**Accuracy:** 48.1%
**Submissions:** 180K+
**Points:** 4
**Average Time:** 15 minutes

---

## 🧩 Problem Statement

Given an array `arr[]` consisting of `n` integers, the task is to **find all the array elements** which occur **more than ⌊n/3⌋ times**.

> Note: The returned array of majority elements should be **sorted**.

---

## 📥 Input

* An array `arr[]` of size `n`.

## 📤 Output

* A sorted array containing all elements that occur more than `n // 3` times.

---

## 💡 Examples

### Example 1:

```
Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
Output: [1, 2]
Explanation: 
The frequency of 1 and 2 is 3, which is more than floor(8/3) = 2.
```

### Example 2:

```
Input: arr[] = [-5, 3, -5]
Output: [-5]
Explanation: 
The frequency of -5 is 2, which is more than floor(3/3) = 1.
```

### Example 3:

```
Input: arr[] = [3, 2, 2, 4, 1, 4]
Output: []
Explanation: 
There is no element with frequency > floor(6/3) = 2.
```

---

## 🧪 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $-10^5 \leq \text{arr}[i] \leq 10^5$

---

## 📈 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

* Bloomberg
* Salesforce
* Accenture
* Microsoft
* TCS
* Google

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Algorithms
* Hashing

---

## 📚 Related Articles

* [Candidates With Majority Vote](https://www.geeksforgeeks.org/find-elements-occurs-array-n3-times/)

---

---

Let's break down everything for the problem **"Majority Element - More Than n/3"**.

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### **Goal**:

Find all elements in the array that appear **more than ⌊n/3⌋ times**.

### **Key Observation**:

In any array of size `n`, there can be **at most 2 elements** that occur more than `n/3` times.
(This is an extension of the **Boyer-Moore Majority Voting Algorithm**).

---

### **Approach: Extended Boyer-Moore Voting Algorithm**

We maintain **2 candidate variables** and **2 counts**:

* Pass 1: Find potential candidates that *may* appear > n/3 times
* Pass 2: Verify if these candidates really occur more than n/3 times

---

### **Dry Run Example**

```python
arr = [2, 2, 3, 1, 3, 2, 1, 1]
n = 8
threshold = n // 3 = 2
```

#### Step 1: Find Potential Candidates

* Start with: `candidate1=None`, `candidate2=None`, `count1=0`, `count2=0`

Now iterate:

```
2 → candidate1=2, count1=1
2 → count1=2
3 → candidate2=3, count2=1
1 → both candidates full, decrement both → count1=1, count2=0
3 → count2=1
2 → count1=2
1 → both candidates full, decrement both → count1=1, count2=0
1 → candidate2=1, count2=1
```

At the end of this phase:

* `candidate1=2`, `candidate2=1`
* These are possible answers

#### Step 2: Count Frequencies Again

* Count of 2 = 3
* Count of 1 = 3

Since both > 2 (n//3), **Output = \[1, 2]**

---

## ✅ 3. Optimized Python Code (Most Expected in Interviews)

```python
from collections import Counter

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        
        # Step 1: Boyer-Moore Voting for two majority candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify actual counts
        result = []
        for c in [candidate1, candidate2]:
            if arr.count(c) > n // 3:
                result.append(c)
        
        return sorted(result)
```

---

### 🔎 Time and Space Complexity

* **Time**: O(n)

  * One pass to choose candidates
  * One pass to verify frequency

* **Space**: O(1)

  * No extra space except for a few variables

---

## ✅ 4. Interview Questions & Answers

### Q1: Why can there be at most 2 majority elements?

**A:** Because if there were 3 numbers each occurring more than n/3 times, the total count would exceed n, which is not possible.

---

### Q2: What if the threshold was `n/4`?

**A:** We would track 3 candidates instead of 2. In general, for `n/k`, track (k-1) candidates.

---

### Q3: Can we use a dictionary instead of Boyer-Moore?

**A:** Yes, a brute-force approach using `Counter` can work in O(n) time but O(n) space.

---

### Brute Force (for completeness, **not preferred** in interviews):

```python
class Solution:
    def findMajority(self, arr):
        from collections import Counter
        n = len(arr)
        freq = Counter(arr)
        res = [x for x in freq if freq[x] > n // 3]
        return sorted(res)
```

* **Time**: O(n)
* **Space**: O(n) (for hashmap)

---

---

# 🌍 Real-World Use Cases

### 1. **Real-Time Analytics (e.g., YouTube, Twitter Trends)**

* **Scenario**: You want to identify videos or hashtags that are **consistently dominating** user interactions (likes, views, hashtags, etc.)
* **Use Case**: Detecting which few trends receive more than 1/3 of all interactions in a given time window using streaming algorithms.
* **Why it matters**: Efficient identification of "viral" content helps prioritize caching, CDN routing, or alerting.

---

### 2. **Voting Systems and Elections**

* **Scenario**: In a national or boardroom election, where a candidate needs to get more than `n/3` votes to avoid a runoff.
* **Use Case**: Quickly detecting candidates with significant public support to optimize ballot analysis or fraud detection.
* **Why it matters**: Allows early detection of frontrunners in streaming or distributed vote counting systems.

---

### 3. **Distributed Consensus Algorithms (e.g., Paxos, Raft)**

* **Scenario**: In distributed systems, consensus often requires quorum agreements.
* **Use Case**: Detecting if any value has been accepted by more than 1/3 of the nodes helps in deciding early consensus failure or majority splits.
* **Why it matters**: Used in fault-tolerant distributed databases like etcd, Apache Cassandra, and blockchain protocols.

---

### 4. **Customer Feedback Systems (e.g., App Ratings, Product Reviews)**

* **Scenario**: You want to find common customer sentiments or repeated product complaints from a large dataset.
* **Use Case**: Identify recurring feedback themes (e.g., "battery", "performance") that appear in >n/3 of responses.
* **Why it matters**: Prioritizes engineering fixes or marketing communication.

---

### 5. **Cybersecurity – Intrusion Detection**

* **Scenario**: In network traffic logs, a few IP addresses or ports may dominate logs during DDoS attacks.
* **Use Case**: Detecting IPs or actions (e.g., failed login attempts) that appear in more than 1/3 of requests quickly.
* **Why it matters**: Enables early threat mitigation in real-time systems.

---
