class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        target = 0
        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = n + nums[l] + nums[r]
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res