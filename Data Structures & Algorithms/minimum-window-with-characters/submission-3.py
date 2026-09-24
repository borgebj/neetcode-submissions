from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = Counter(t)
        window_freq = Counter()
        
        best_len = float("inf")
        best_left = float("inf")

        # distinct characters
        need = len(target_freq)
        have = 0

        left = 0
        for right in range(len(s)):

            # adds character to counter
            window_freq[s[right]] += 1
            if window_freq[s[right]] == target_freq[s[right]]:
                have += 1

            # shrink window while its valid
            # to shorten as much as possible
            while have == need:

                # save position of best window
                win_len = right - left + 1
                if win_len < best_len:
                    best_len = win_len
                    best_left = left

                if window_freq[s[left]] == target_freq[s[left]]:
                    have -= 1
                
                window_freq[s[left]] -= 1
                left += 1
        
        if best_left == float("inf"):
            return ""
        
        return s[best_left:best_left + best_len]

# finds smallest window containing all characters in t:
# s = "aabdc", t = "abc"
#
# strategy:
#   - expand right until valid
#   - save window
#   - shrink left while valid
#
# target_freq = {a:1, b:1, c:1}
#
# [a, a, b, d, c] -> {a:1} invalid
#  ^  ^
# [a, a, b, d, c] -> {a:2, b:1} invalid
#  ^     ^
# [a, a, b, d, c] -> {a:2, b:1, d:1} invalid
#  ^        ^
# [a, a, b, d, c] -> {a:2, b:1, c:1, d:1} valid, best = 5
#  ^           ^
# [a, a, b, d, c] -> {a:1, b:1, c:1, d:1} valid, best = 4
#     ^        ^
# [a, a, b, d, c] -> {b:1, c:1, d:1} invalid
#        ^     ^

