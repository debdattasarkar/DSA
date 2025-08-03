class Solution:
    def cntCoprime(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        
        # Step 1: Find max value to define limits of our frequency arrays
        m = max(arr)

        # Step 2: Frequency of each number
        l = [0] * (m + 1)  # l[x] stores frequency of x in array
        for x in arr:
            l[x] += 1

        # Step 3: r[i] stores number of pairs (a, b) such that both a and b are divisible by i
        r = [0] * (m + 1)

        # Step 4: Inclusion-Exclusion to count valid (a, b) pairs for each i
        for i in range(m, 0, -1):
            c = 0
            for j in range(i, m + 1, i):
                r[i] -= r[j]      # Subtract over-counted from multiples
                c += l[j]         # Count numbers divisible by i
            r[i] += (c * (c - 1)) // 2  # Choose 2 from c to form unordered pairs

        return r[1]  # r[1] gives count of all coprime pairs (gcd = 1)