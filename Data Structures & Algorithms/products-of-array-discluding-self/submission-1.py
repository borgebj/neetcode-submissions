class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prods = []
        prefix = [0] * n; prefix[0] = nums[0]
        suffix = [0] * n; suffix[n-1] = nums[n-1]

        # build prefix array
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
            
        # build suffix array
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        # build product list excluding i
        for i in range(n):
            # start
            if i == 0:
                prods.append(suffix[1])
            # end
            elif i == n - 1:
                prods.append(prefix[n-2])
            # middle
            else:
                prods.append(prefix[i-1] * suffix[i+1])
        
        return prods