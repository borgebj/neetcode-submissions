class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a list of seen numbers
        seen = set()

        # if seen before return true, else add in seen
        for num in nums:
            if num in seen: 
                return True
            else:
                seen.add(num)

        return False