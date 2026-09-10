class Solution:

    # gives prefix maximum array
    def prefMax(self, nums):
        prefix_max = []
        curr_max = float("-inf")

        for num in nums:
            curr_max = max(curr_max, num)
            prefix_max.append(curr_max)
        
        return prefix_max

    # gives suffix maximum array
    def sufMax(self, nums):
        suffix_max = []
        curr_max = float("-inf")

        for num in reversed(nums):
            curr_max = max(curr_max, num)
            suffix_max.append(curr_max)

        suffix_max.reverse()
        return suffix_max


    def trap(self, height: List[int]) -> int:

        # uses suffix and prefix maximum arrays 
        pref = self.prefMax(height) 
        suff = self.sufMax(height)

        total = 0

        for i, num in enumerate(height):
            
            # calculate water by looking at greatest left, greatest right
            # then subtracting current height
            total += min(pref[i], suff[i]) - num

        return total