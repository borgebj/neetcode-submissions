from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target_freq = Counter(t)
        window_freq = Counter()

        have = 0
        need = len(target_freq)
        
        best_len = float("inf")
        best_left = float("inf")

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_freq[char] += 1

            if char in target_freq and window_freq[char] == target_freq[char]:
                have += 1

            # shrink window while its valid
            # to shorten as much as possible
            while have == need:

                # save position of best window
                win_len = right - left + 1
                if win_len < best_len:
                    best_len = win_len
                    best_left = left

                char = s[left]
                window_freq[char] -= 1

                if char in target_freq and window_freq[char] < target_freq[char]:
                    have -= 1                

                left += 1
        
        if best_left == float("inf"):
            return ""

        return s[best_left:best_left + best_len]

# finds smallest window containing all characters in t:
# s = "adobecodebanc", t = "abc"
#
# strategy:
#   - expand right until valid
#   - save window
#   - shrink left while valid
#
