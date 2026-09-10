class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort so we can use twosum pointers
        nums = sorted(nums)

        solutions = set()

        for i in range(len(nums)):

            # skips duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # with target, perform twosum pointer algorithm
            target = -nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                twosum = nums[left] + nums[right]

                # target found, add to solution as tuple to ensure no duplicates
                if twosum == target:
                    solution = (nums[i], nums[left], nums[right])
                    solutions.add(solution)

                    left += 1
                    right -=1

                # if target is greater, right pointer moves down
                elif twosum > target:
                    right -= 1

                # if target is less, left pointer goes up
                else:
                    left += 1
                
        return [list(x) for x in solutions]

