class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        # pointer at start and end
        while left < right:
            
            # compare two pointer numbers
            twosum = numbers[left] + numbers[right]
            
            if twosum == target:
                return [left + 1, right + 1]

            # if sum greater: move end-pointer down    
            elif twosum > target:
                right -= 1
            
            # if sum less: move start-pointer up
            else:
                left += 1
            
        return []