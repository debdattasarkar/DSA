class Solution:
    def isValid(self, s):
        # Split by '.' and ensure exactly 4 groups
        parts = s.split('.')
        if len(parts) != 4:
            return False

        for p in parts:
            # 1) non-empty, 2) digits only
            if not p or not p.isdigit():
                return False

            # 3) no leading zeros unless the group is exactly "0"
            if len(p) > 1 and p[0] == '0':
                return False

            # 4) numeric range 0..255
            val = int(p)
            if val < 0 or val > 255:
                return False

        # All 4 parts passed validation
        return True