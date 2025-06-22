class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for placing the next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Copy valid element forward
                k += 1  # Move to next placement index
        return k  # New length of valid elements