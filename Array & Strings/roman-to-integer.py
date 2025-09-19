# define dictionary and total variable
# iterate over the string
# get current and next value (if applicable)
# if current is lesser than next, rest total to current value
# else sum total to current value

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i in range(len(s)):
            crr, nxt = dic[s[i]], dic[s[i + 1]] if i + 1 < len(s) else 0
            if crr < nxt:
                total -= crr
            else:
                total += crr

        return total