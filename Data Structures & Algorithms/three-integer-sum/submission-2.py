class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        solutions = set()

        # solution 1: brute-force

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    combination = tuple(sorted([nums[i], nums[j], complement]))
                    solutions.add(combination)
                
                seen.add(nums[j])
        
        return [list(x) for x in solutions]