from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        top_k = []
        n = len(nums)
        counts = defaultdict(int)
        bucket = [[] for _ in range(n+1)]

        # 1. count frequencies
        for num in nums:
            counts[num] += 1
            
        # 2. put in buckets based on frequencies
        for num, count in counts.items():
            bucket[count].append(num)
            
        # 3. start at highest frequency and go down (backwards)
        for i in range(n, 0, -1):
            for num in bucket[i]:
                top_k.append(num)
            
            if len(top_k) == k: 
                break
                
        return top_k