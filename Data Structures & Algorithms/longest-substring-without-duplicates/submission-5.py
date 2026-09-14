class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best = 0
        left = 0
        window = set()

        # check sequences using a window:
        # [a, b, c, a, b] -> valid, move right pointer
        #  ^  ^
        # [a, b, c, a, b] -> valid, move right pointer
        #  ^     ^
        # [a, b, c, a, b] -> invalid, move left until valid
        #  ^        ^
        # [a, b, c, a, b] -> valid, move right pointer
        #     ^     ^
        # [a, b, c, a, b] -> invalid, move left until valid
        #     ^        ^
        # [a, b, c, a, b] -> valid, end of list
        #        ^     ^
        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            best = max(best, len(window))

        return best