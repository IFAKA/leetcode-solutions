class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # initial state
        balloon_len = 7

        # edge cases
        if len(text) < balloon_len:
            return 0

        # return
        return min(
            text.count("b"),
            text.count("a"),
            text.count("l") // 2,
            text.count("o") // 2,
            text.count("n"),
        )

        # SC: O(1) TC: O(n)
