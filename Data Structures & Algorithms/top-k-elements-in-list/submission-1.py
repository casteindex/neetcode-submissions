class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = [(value, key) for key, value in count.items()]
        top_frequent = heapq.nlargest(k, heap)
        res = [value for key, value in top_frequent]

        return res