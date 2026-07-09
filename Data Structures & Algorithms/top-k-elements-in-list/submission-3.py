class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # Ordernar numeros por cuenta usando bucket sort
        buckets = [[] for _ in range(max(counts.values()) + 1)]
        for n, count in counts.items():
            buckets[count].append(n)

        sorted_nums = []
        for bucket in buckets:
            for n in bucket:
                sorted_nums.append(n)
        
        return sorted_nums[-k:]
        