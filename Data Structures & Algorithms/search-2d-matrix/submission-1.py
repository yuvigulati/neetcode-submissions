class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row - 1
        correct_row = -1 
        while lo <= hi:
            middle  = (hi + lo) // 2

            if target < matrix[middle][0]:
                hi = middle - 1
            elif target > matrix[middle][-1]:
                lo = middle + 1
            else:
                correct_row = middle
                break
        
        if correct_row == -1:
            return False

        lo, hi = 0, col - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[correct_row][mid] == target:
                return True
            elif matrix[correct_row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
            

        

        
