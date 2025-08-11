class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        moves = []

        def solve(k, a, b, c):
            if k == 0:
                return
            solve(k - 1, a, c, b)
            moves.append((k, a, b))  # compact tuple if you prefer
            solve(k - 1, c, b, a)

        solve(n, fromm, to, aux)
        return len(moves)  # <- important for your case