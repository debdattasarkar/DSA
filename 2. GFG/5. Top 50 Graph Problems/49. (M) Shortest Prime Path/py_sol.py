
#User function Template for python3
from collections import deque

class Solution:
    def solve (self,Num1,Num2):
        """
        Straight BFS on implicit graph of 4-digit primes.
        Time:  O( P * 40 ) roughly, where P is number of 4-digit primes (~1061)
               Each node generates up to 36-40 candidates (4 positions * up to 10 digits).
        Space: O(P)
        """

        # Quick exit
        if Num1 == Num2:
            return 0

        # 1) Sieve: primality up to 9999 (we only care 1000..9999)
        MAXN = 10000
        is_prime = [True] * MAXN
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(MAXN**0.5) + 1):
            if is_prime[p]:
                step = p
                start = p * p
                for x in range(start, MAXN, step):
                    is_prime[x] = False

        # Ensure inputs fit the domain
        if not (is_prime[Num1] and is_prime[Num2]):
            # Per problem statement both are primes; this is defensive.
            return -1

        # 2) BFS setup
        q = deque()
        q.append((Num1, 0))  # (current_prime, distance)
        visited = set([Num1])

        # Helper to generate one-digit-different prime neighbors
        def neighbors(x: int):
            s = list(str(x))
            for i in range(4):
                original = s[i]
                for d in '0123456789':
                    if d == original:
                        continue
                    if i == 0 and d == '0':  # no leading zero
                        continue
                    s[i] = d
                    y = int(''.join(s))
                    if is_prime[y]:
                        yield y
                s[i] = original

        # 3) BFS loop
        while q:
            cur, dist = q.popleft()
            for nxt in neighbors(cur):
                if nxt in visited:
                    continue
                if nxt == Num2:
                    return dist + 1
                visited.add(nxt)
                q.append((nxt, dist + 1))

        # If unreachable
        return -1