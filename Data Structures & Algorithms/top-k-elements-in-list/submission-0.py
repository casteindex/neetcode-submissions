class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res: list[int] = []
        for i in range(k):
            n_max_count = max(count, key=count.get)
            res.append(n_max_count)
            del count[n_max_count]
        
        return res