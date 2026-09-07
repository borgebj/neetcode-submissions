class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        all_longest = []
        longest = 1

        # sort
        nums.sort()

        # check for sequences in sorted list
        for i in range(len(nums) - 1):
            curr_num = nums[i]
            next_num = nums[i+1]

            if curr_num == next_num: 
                continue

            if (next_num == curr_num+1):
                longest += 1
            else:
                all_longest.append(longest)
                longest = 1
            
        all_longest.append(longest)
        
        return max(all_longest)
