class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums) - 1 

        if len(nums) < 3:
            if nums[lo] == target:
                return lo
            elif nums[hi] == target:
                return hi
            else:
                return -1
            

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid 
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1 
        return -1

