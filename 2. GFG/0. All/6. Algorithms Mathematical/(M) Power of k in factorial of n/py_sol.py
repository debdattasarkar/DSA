class Solution:
	def maxKPower(self, n, k):
		# code here
        # Function to factorize k into prime powers
        def prime_factors(k):
            i = 2
            factors = {}
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        # Legendre's formula to count power of p in n!
        def count_power_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        factors = prime_factors(k)
        min_power = float('inf')

        for p, a in factors.items():
            power_in_fact = count_power_in_factorial(n, p)
            min_power = min(min_power, power_in_fact // a)

        return min_power