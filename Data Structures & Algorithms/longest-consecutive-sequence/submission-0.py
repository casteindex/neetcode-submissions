class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)

        starts: list[int] = []
        for n in nums_s:
            if (n - 1) not in nums_s:
                starts.append(n)
        
        max_length = 0
        for n in starts:
            curr_n, length = n, 1
            while (curr_n + 1) in nums_s:
                length += 1
                curr_n += 1
            max_length = max(max_length, length)
        
        return max_length
