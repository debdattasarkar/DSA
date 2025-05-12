#User function Template for python3

class Solution:
    # Function to calculate minimum energy needed.
    def minEnergy(self, arr):
        # Your code goes here
        energy = 0       # Cumulative energy level
        min_energy = 0   # Track the lowest point of energy

        for value in arr:
            energy += value
            min_energy = min(min_energy, energy)  # Update lowest energy seen

        # We need at least 1 more than the lowest point
        return abs(min_energy) + 1

#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().minEnergy(a))
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends