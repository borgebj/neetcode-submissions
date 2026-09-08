class Solution:
    def maxArea(self, heights: List[int]) -> int:

        highest = 0
        
        left = 0
        right = len(heights) - 1

        while left < right:

            a = heights[left]
            b = heights[right]

            vol = (right - left) * min(a, b)

            if vol > highest:
                highest = vol

            if a < b:
                left += 1
            else:
                right -= 1
        return highest