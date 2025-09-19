class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # edge cases
        if len(magazine) < len(ransomNote):
            return False
        # init state
        char_count = {char: magazine.count(char) for char in set(magazine)}
        # loop validations return true false
        for note in ransomNote:
            if note in char_count and char_count[note] > 0:
                char_count[note] -= 1
            else:
                return False
        return True

# Input: 
# ransomNote = "aach",

# magazine = "aabc"
# char_count a:2, b:1, c:1
# char_count a:1, b:1, c:1
# char_count a:0, b:1, c:1
# char_count a:0, b:0, c:1


