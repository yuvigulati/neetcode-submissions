class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        if len(nums) == 0:
            return 0

        for i in hash_set:
            if i - 1 not in hash_set:
                current_num = i
                current_length = 1

                while current_num + 1 in hash_set:
                    current_length += 1
                    current_num += 1

                longest = max(longest, current_length)
        return longest


                
            



