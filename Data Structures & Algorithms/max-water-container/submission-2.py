class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            temp_area = 0
            if heights[i] < heights[j]:
                temp_area = heights[i] * abs((j - i))
                i += 1
            else:
                temp_area = heights[j] * abs((j - i))
                j -= 1
            max_area = max(temp_area, max_area)
            
        return max_area
            
            

        