import heapq
class Solution:
  def minOperations(self, arr):
    """
    Greedy: repeatedly halve the current largest element.
    Use a max-heap (store negatives since Python heapq is min-heap).
    Time:  O(n + k*log n), where k = number of operations performed
    Space: O(n)
    """
    total_sum = sum(arr)
    target = total_sum / 2.0

    # Build max-heap
    max_heap = [-x for x in arr]  # negatives for max behavior
    heapq.heapify(max_heap)       # O(n)

    ops = 0
    current_sum = total_sum

    # Keep reducing until we cross the target
    while current_sum > target:
        largest = -heapq.heappop(max_heap)  # O(log n)
        halved = largest / 2.0              # float allowed
        current_sum -= halved               # drop = largest/2
        heapq.heappush(max_heap, -halved)   # O(log n)
        ops += 1

    return ops