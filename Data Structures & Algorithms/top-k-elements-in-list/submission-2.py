from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        top_k = []

        for num in nums:
            counts[num] += 1

        # custom sorts dict based on frequency, highest first
        frequencies = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # return only first k
        return [num for num, count in frequencies[:k]]