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