class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            lHeight, rHeight = heights[l], heights[r]
            currArea = min(lHeight, rHeight) * (r - l)
            maxArea = max(maxArea, currArea)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
        return maxArea