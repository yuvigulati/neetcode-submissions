class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        heap = []
        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict[num] += 1
        
        for key, val in new_dict.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return[val for k, val in heap]
