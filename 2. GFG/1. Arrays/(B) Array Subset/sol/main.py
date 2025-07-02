from collections import Counter

class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):

        # Step 1: Count frequency of each element in array 'a'
        freq = Counter(a)  # Time: O(n), Space: O(n), where n = len(a)

        # Step 2: For each element in array 'b', check and consume from freq map
        for num in b:  # Time: O(m), where m = len(b)
            if freq[num] == 0:
                return False  # Element missing or already consumed
            freq[num] -= 1  # Use one occurrence of that element

        return True  # All elements in b[] are accounted for in a[]
    
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    a1 = [11, 1, 13, 21, 3, 7]
    b1 = [11, 3, 7, 1]
    print("a:", a1)
    print("b:", b1)
    print("Output:", sol.isSubset(a1, b1))  # Expected: True

    # Test Case 2
    a2 = [1, 2, 3, 4, 5]
    b2 = [1, 2, 6]
    print("\na:", a2)
    print("b:", b2)
    print("Output:", sol.isSubset(a2, b2))  # Expected: False

    # Test Case 3 (duplicates)
    a3 = [2, 2, 3, 4]
    b3 = [2, 2, 3]
    print("\na:", a3)
    print("b:", b3)
    print("Output:", sol.isSubset(a3, b3))  # Expected: True

    # Test Case 4 (b has more of an element than a)
    a4 = [2, 3, 2]
    b4 = [2, 2, 2]
    print("\na:", a4)
    print("b:", b4)
    print("Output:", sol.isSubset(a4, b4))  # Expected: False