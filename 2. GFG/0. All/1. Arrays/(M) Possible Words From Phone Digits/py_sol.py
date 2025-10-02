class Solution:
    def possibleWords(self, arr):
        """
        Backtracking over digit->letters, **skipping digits 0 and 1**.
        Time:  O(4^n) in the number of mapped digits
        Space: O(n) recursion + O(#answers * n) output
        """
        if not arr:
            return []

        phone = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }

        # Build the pools; SKIP digits with no mapping (0 and 1)
        pools = []
        for d in arr:
            if d in phone:
                pools.append(phone[d])
            else:
                # skip 0/1
                continue

        # If there were only 0/1s, no words can be formed
        if not pools:
            return []

        res, path = [], []

        def dfs(i: int):
            if i == len(pools):
                res.append("".join(path))
                return
            for ch in pools[i]:
                path.append(ch)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res