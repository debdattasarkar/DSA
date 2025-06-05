class ArrayManager:
    def __init__(self):
        self.arr = []  # Use a dynamic list (no fixed size)

    def insert(self, value):
        if len(self.arr) < 10:
            self.arr.append(value)
        else:
            print("Array is full, cannot insert more elements!")

    def display(self):
        print("Array elements:", self.arr)

    def search(self, value):
        return value in self.arr

    def remove(self, value):
        if value in self.arr:
            self.arr.remove(value)
            print(f"Element {value} deleted successfully.")
        else:
            print("Element not found, cannot delete!")

    def find_smallest(self):
        if not self.arr:
            print("Array is empty!")
            return None
        return min(self.arr)

    def find_largest(self):
        if not self.arr:
            print("Array is empty!")
            return None
        return max(self.arr)
    
    def reverse_array(self):
        if not self.arr:
            print("Array is empty!")
            return None
        else:
            self.arr = self.arr[::-1]

    # Missing number finder
    def findMissingNumber(self):
        if not self.arr:
            print("Array is empty!")
            return None
        n = len(self.arr)
        maxNum = n + 1  # Since one number is missing
        expectedSum = maxNum * (maxNum + 1) // 2  # Integer division
        actualSum = sum(self.arr)  # Cleaner!
        return expectedSum - actualSum
    
    
def main():
    am = ArrayManager()

    am.insert(1)
    am.insert(2)
    am.insert(4)
    am.insert(5)

    am.display()

    # print("Searching for 3:", "Found" if am.search(3) else "Not Found")
    # print("Searching for 10:", "Found" if am.search(10) else "Not Found")

    # am.remove(9)

    # print("After Reversing:")
    # am.reverse_array()
    # am.display()

    # print("Smallest number:", am.find_smallest())
    # print("Largest number:", am.find_largest())
    print("Missing number:", am.findMissingNumber())

if __name__ == "__main__":
    main()