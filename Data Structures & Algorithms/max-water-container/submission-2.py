class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights) - 1
        max_vol = 0

        while i < j:
            cur_vol = min(heights[i],heights[j]) * (j-i)
            if cur_vol > max_vol:
                max_vol = cur_vol
            elif heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_vol