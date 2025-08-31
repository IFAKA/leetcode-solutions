class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Algorithm:
        # 1. Handle edge cases (empty s or t).
        # 2. Use a pointer to track position in s.
        # 3. Iterate through t, advancing pointer on matches.
        # 4. Return True if all characters of s are found (pointer reaches len(s)).
        # 5. Return False otherwise.
        
        if not s:
            return True
        if not t or len(s) > len(t):
            return False
        
        j = 0
        for char in t:
            if j < len(s) and char == s[j]:
                j += 1
            if j == len(s):
                return True
        
        return j == len(s)