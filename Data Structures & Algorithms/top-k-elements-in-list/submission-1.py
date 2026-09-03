from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        top_k = []

        for num in nums:
            counts[num] += 1

        # 4. repeat k times
        for _ in range(k):
            
            # 1. get highest key based on value
            highest = max(counts, key=counts.get)

            # 2. add to top_k
            top_k.append(highest)

            # 3. remove it from counts
            highest = counts.pop(highest)
        
        return top_k

# example: 
# nums = [a,a, b,b,b c,c,c,c]
# k = 2
#
# counts = {a:1, b:2, c:4}
# highest = c:4 -> [c]
# 
# counts = {a:1, b:2}
# highest = b:2 -> [c, b]