class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s -> t
        # edge cases
        if len(s) != len(t):
            return False
        
        # inital states
        ana_list = { char: s.count(char) for char in set(s) }

        # loop and validate
        for letter in t:
            if letter in ana_list and ana_list[letter] > 0:
                ana_list[letter] -= 1
            else:
                return False
        
        return True