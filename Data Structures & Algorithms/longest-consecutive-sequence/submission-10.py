from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # nums as a set, so no duplicates
        nums_set = set(nums)
        longest = 0

        # go through nums, check for successor numbers
        for num in nums_set:

            # check beginning of sequence
            if num - 1 not in nums_set:
                current = num
                length = 1

                # search for sequence
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                
                longest = max(longest, length)

        return longest  
        