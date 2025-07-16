class Solution:
    def countNumbers(self, n):
        # code here
        # Step 1: Sieve of Eratosthenes to get primes up to sqrt(n)
        import math
        limit = int(math.sqrt(n)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i*i, limit+1, i):
                    is_prime[j] = False

        primes = [i for i, prime in enumerate(is_prime) if prime]

        count = 0

        # Pattern 1: p^8
        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break  # No need to continue further

        # Pattern 2: p^2 * q^2 where p != q
        len_primes = len(primes)
        for i in range(len_primes):
            for j in range(i+1, len_primes):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    count += 1
                else:
                    break  # inner loop break

        return count