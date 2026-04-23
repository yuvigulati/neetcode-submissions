class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_i, max_j = 0, 0
        total_sum = 0

        while i < j:
            if height[i] <= height[j]:
                if max_i <= height[i]:
                    max_i = height[i]
                else:
                    total_sum += max_i - height[i]
                i +=1
            else:
                if max_j <= height[j]:
                    max_j = height[j]
                else:
                    total_sum += max_j - height[j]  
                j -= 1
        return total_sum
                    


            

            
            

