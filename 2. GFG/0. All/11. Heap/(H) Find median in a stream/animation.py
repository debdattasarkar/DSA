# Re-importing libraries after kernel reset
import matplotlib.pyplot as plt
import heapq
import matplotlib.animation as animation

# Stream of integers
arr = [5, 15, 1, 3, 2, 8]

# Max heap and min heap (inverted logic for max heap)
low = []  # max-heap
high = []  # min-heap
medians = []

# Prepare step-by-step heap states
heap_steps = []

for num in arr:
    if not low or num <= -low[0]:
        heapq.heappush(low, -num)
    else:
        heapq.heappush(high, num)

    # Rebalance heaps
    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

    # Calculate median
    if len(low) == len(high):
        median = (-low[0] + high[0]) / 2.0
    else:
        median = float(-low[0])

    medians.append(median)
    # Store a copy of current heap states
    heap_steps.append((list(-x for x in low), list(high)))

# Animation function
fig, ax = plt.subplots()
bar_low = ax.bar([], [], label='Max Heap (low)', color='skyblue')
bar_high = ax.bar([], [], label='Min Heap (high)', color='salmon')
text = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center')
ax.legend(loc='upper right')

def update(frame):
    ax.clear()
    low_heap, high_heap = heap_steps[frame]
    ax.bar(range(len(low_heap)), sorted(low_heap, reverse=True), color='skyblue', label='Max Heap (low)')
    ax.bar(range(len(low_heap), len(low_heap) + len(high_heap)), sorted(high_heap), color='salmon', label='Min Heap (high)')
    ax.set_ylim(0, max(arr) + 5)
    ax.set_title(f'Step {frame + 1} - Insert {arr[frame]} | Median: {medians[frame]}')
    ax.legend(loc='upper right')

ani = animation.FuncAnimation(fig, update, frames=len(heap_steps), repeat=False)
plt.close(fig)
ani
