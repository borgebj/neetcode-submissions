from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i, num in enumerate(numbers):

            # calculates complement
            complement = (target - num)

            # looks for complement
            if complement in d:
                return [d[complement], i+1]

            d[num] = i+1
        
        return []