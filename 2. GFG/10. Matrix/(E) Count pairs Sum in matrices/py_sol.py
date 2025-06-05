class Solution:
    def countPairs(self, mat1, mat2, x):
        # code here
        # Flatten mat2 into a set for O(1) lookups
        mat2_values = set()
        for row in mat2:
            mat2_values.update(row)

        count = 0
        # Check for each element in mat1 if x - element exists in mat2
        for row in mat1:
            for val in row:
                if (x - val) in mat2_values:
                    count += 1

        return count