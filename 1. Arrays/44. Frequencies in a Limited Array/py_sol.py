class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        n = len(arr)

        # Initialize a frequency list with zeros
        freq = [0] * n

        # Count occurrences for values between 1 and n
        for num in arr:
            if 1 <= num <= n:
                freq[num - 1] += 1  # Map value x to index x-1

        return freq


# Driver code
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))
    result = Solution().frequencyCount(arr)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("[]")
