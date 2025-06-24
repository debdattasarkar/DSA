import random

class RandomizedSet:

    def __init__(self):
        self.idx_map = {}  # val -> index
        self.nums = []     # stores values

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        # Move last element to val's position and pop last
        last_val = self.nums[-1]
        idx = self.idx_map[val]
        self.nums[idx] = last_val
        self.idx_map[last_val] = idx
        self.nums.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()