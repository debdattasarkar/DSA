class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionary to track character mapping from s -> t and t -> s
        map_s_t = {}
        map_t_s = {}
        
        for cs, ct in zip(s, t):
            # Check if mapping exists and is consistent from s to t
            if cs in map_s_t:
                if map_s_t[cs] != ct:
                    return False
            else:
                map_s_t[cs] = ct
            
            # Check reverse mapping from t to s
            if ct in map_t_s:
                if map_t_s[ct] != cs:
                    return False
            else:
                map_t_s[ct] = cs
        
        return True