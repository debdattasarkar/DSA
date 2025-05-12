To solve the **Meeting Rooms III** problem from GeeksforGeeks, we simulate room assignment while keeping track of:

* When each room becomes available.
* Which room has hosted the most meetings.

---

## ✅ Problem Summary

You're given:

* `n` rooms (`0` to `n-1`)
* `meetings[i] = [starti, endi]`

**Goal**: Find the room with the most meetings.
If a tie, return the room with the smallest number.

**Rules**:

* Assign the meeting to the earliest available room (smallest number).
* If no room is free, delay it until the earliest room is free but retain the meeting's duration.
* Always prioritize assigning to rooms with the smallest number.

---

## 🔍 Strategy

Use two heaps:

* **Available Rooms Min-Heap** → Sorted by room number.
* **Occupied Rooms Min-Heap** → `(end_time, room_number)`.

Use a `meeting_count[]` array to track how many meetings each room has hosted.

### Steps:

1. **Sort meetings by start time.**
2. **Initialize** available rooms heap with all room numbers.
3. For each meeting:

   * Release rooms that are now available (i.e., their end time is <= current meeting's start).
   * If available rooms exist, assign the meeting to the smallest room.
   * If all rooms are occupied, **delay** the meeting until the earliest one is free and **reschedule** accordingly.
4. Track how many meetings each room is assigned.
5. Return the room with the maximum count (and smallest room number in case of tie).

---

## 🔄 Dry Run

`n = 2`
`meetings = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]`

Meeting 0: assign to room 0
Meeting 1: room 1 is free → assign
Meeting 2: room 1 is free → assign
Meeting 3: no room free → delay until 6 → assign to room 0
Meeting 4: no room free → delay until 7 → assign to room 1

Room usage:

* Room 0: 2 meetings
* Room 1: 3 meetings → return **1**

---

## ✅ Python Code with Comments

```python
import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()  # Sort by start time

        # Available rooms by room number
        available = list(range(n))
        heapq.heapify(available)

        # Busy rooms as (end_time, room_id)
        busy = []

        # Count of meetings per room
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that are now available
            while busy and busy[0][0] <= start:
                end_time, room_id = heapq.heappop(busy)
                heapq.heappush(available, room_id)

            if available:
                # Assign to earliest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                # Delay: take earliest finishing room
                end_time, room = heapq.heappop(busy)
                duration = end - start
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
                count[room] += 1

        # Find room with max count, prefer lower room number
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
```

---

## ✅ C++ Version with Inline Comments

```cpp
class Solution {
  public:
    int mostBooked(int n, vector<vector<int>> &meetings) {
        sort(meetings.begin(), meetings.end());

        priority_queue<int, vector<int>, greater<int>> available;
        for (int i = 0; i < n; ++i) available.push(i);

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> busy;

        vector<int> count(n, 0);

        for (auto &m : meetings) {
            long long start = m[0], end = m[1];

            while (!busy.empty() && busy.top().first <= start) {
                available.push(busy.top().second);
                busy.pop();
            }

            if (!available.empty()) {
                int room = available.top(); available.pop();
                busy.push({end, room});
                count[room]++;
            } else {
                auto [free_time, room] = busy.top(); busy.pop();
                long long duration = end - start;
                busy.push({free_time + duration, room});
                count[room]++;
            }
        }

        int max_meetings = 0, result = 0;
        for (int i = 0; i < n; ++i) {
            if (count[i] > max_meetings) {
                max_meetings = count[i];
                result = i;
            }
        }
        return result;
    }
};
```

---

## ✅ JavaScript Version

```javascript
class Solution {
    mostBooked(n, meetings) {
        meetings.sort((a, b) => a[0] - b[0]);

        const available = [...Array(n).keys()].sort((a, b) => a - b);
        const busy = new MinPriorityQueue({ priority: x => x[0] }); // [end_time, room_id]

        const count = Array(n).fill(0);

        for (let [start, end] of meetings) {
            // Free up rooms
            while (!busy.isEmpty() && busy.front().element[0] <= start) {
                let room = busy.dequeue().element[1];
                available.push(room);
                available.sort((a, b) => a - b); // keep min-heap behavior
            }

            if (available.length > 0) {
                let room = available.shift();
                busy.enqueue([end, room]);
                count[room]++;
            } else {
                let [end_time, room] = busy.dequeue().element;
                let new_end = end_time + (end - start);
                busy.enqueue([new_end, room]);
                count[room]++;
            }
        }

        let max = Math.max(...count);
        for (let i = 0; i < n; i++) {
            if (count[i] === max) return i;
        }
    }
}
```

---

Would you like this solution illustrated with a diagram for delayed meetings and heap updates?
