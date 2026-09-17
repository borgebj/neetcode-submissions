from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # window size
        k = len(s1)

        # uses counters as in-place frequency counters
        target_freq = Counter(s1)
        window_freq = Counter()
        
        left = 0
        for right in range(len(s2)):
            window_freq[s2[right]] += 1
            
            # a constant sliding window of size k (length of s1)
            if right - left + 1 == k:

                # if both frequency counters are identical, a valid permutation exist
                if window_freq == target_freq:
                    return True

                window_freq[s2[left]] -= 1

                # remove 0 entries
                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]

                left += 1

        return False

    
# checks permutations using a fixed-size window
# s1 = "ab" s2 = "eidbaoo"
# strategy:
#   - keep window size == len(s1) = k
#   - compare window frequency with target frequency
#   - remove left chater when window moves
#
# [e, i, d, b, a, o, o] -> no match
#  ^  ^
# window_freq = {e:1, i:1} != {a:1, b:1} = target_freq
#
# [e, i, d, b, a, o, o] -> no match
#     ^  ^
# window_freq = {i:1, d:1} != {a:1, b:1} = target_freq
#
# [e, i, d, b, a, o, o] -> no match
#        ^  ^
# window_freq = {d:1, b:1} != {a:1, b:1} = target_freq
#
# [e, i, d, b, a, o, o] -> Match
#           ^  ^
# window_freq = {b:1, a:1} == {a:1, b:1} = target_freq