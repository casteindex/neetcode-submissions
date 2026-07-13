class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        max_length = 0

        for n in nums_s:
            if n - 1 not in nums_s:
                length = 1
                while n + length in nums_s:
                    length += 1
                max_length = max(max_length, length)
                
        return max_length