class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, 1
        largestArea = 0
        currArea = 0
        while l < r and r != len(heights):
            lHeight = heights[l]
            rHeight = heights[r]
            if lHeight < rHeight:
                currArea = lHeight * (r - l)
            else:
                currArea = rHeight * (r - l)
            if currArea > largestArea:
                largestArea = currArea
            if r != len(heights) - 1:
                r += 1
            else:
                l += 1
                r = l + 1
        return largestArea