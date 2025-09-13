#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()  # Step 1: Sort the array
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return False  # No triplet found