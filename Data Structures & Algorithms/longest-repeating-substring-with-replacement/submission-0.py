from collections import defaultdict 

class Solution: 
    def characterReplacement(self, s: str, k: int) -> int: 
        best = 0 
        left = 0 
        
        highest_freq = 0    # keep track of highest freq at all time 
        frequency = defaultdict(int) 
        
        # sliding window checking no. replacements needed compared to K 
        
        for right in range(len(s)): 
            # update frequencies 
            frequency[s[right]] += 1 
            highest_freq = max(highest_freq, frequency[s[right]]) 
            
            win_len = right - left + 1 
            diff = win_len - highest_freq 
            
            # move window when replacements needed exceed K 
            while diff > k: 
                # update frequencies 
                frequency[s[left]] -= 1 
                left += 1 
                
                # recalculate diff 
                win_len = right - left + 1 
                diff = win_len - highest_freq 
                
            best = max(best, win_len) 
    
        return best