#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()  # Sort the array
        n = len(arr)

        for i in range(n - 2):  # Fix the first element
            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == target:
                    return True  # Triplet found

                elif total < target:
                    left += 1  # Need a bigger sum
                else:
                    right -= 1  # Need a smaller sum

        return False