# Handle edge cases (empty array or single string).
# Use the first string as the initial prefix.
# For each subsequent string, check if the prefix matches its start.
# If not, shorten the prefix by one character and repeat until it matches or becomes empty.
# Return the final prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for word in strs:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix