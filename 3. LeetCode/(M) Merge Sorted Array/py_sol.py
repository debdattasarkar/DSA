class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Merge nums1 and nums2 using a heap. Modify nums1 in-place.
        """
        # Take only the first m valid elements from nums1
        heap = nums1[:m] + nums2[:n]  # Combine valid parts
        
        heapq.heapify(heap)  # Build a min-heap from combined list
        
        # Replace nums1's contents in sorted order
        for i in range(m + n):
            nums1[i] = heapq.heappop(heap)