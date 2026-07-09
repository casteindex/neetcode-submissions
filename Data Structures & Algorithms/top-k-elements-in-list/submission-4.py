class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = {}
        max_count = 0
        for n in nums:
            new_count = 1 + counts.get(n, 0)
            counts[n] = new_count
            max_count = max(max_count, new_count)

        # Ordernar numeros por cuenta usando bucket sort
        buckets = [[] for _ in range(max_count + 1)]
        for n, count in counts.items():
            buckets[count].append(n)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
