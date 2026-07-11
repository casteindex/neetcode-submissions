class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [1]
        for i in range(len(nums)):
            forward.append(nums[i] * forward[i])
        
        temp = nums[::-1]
        backwards = [1]
        for i in range(len(nums)):
            backwards.append(temp[i] * backwards[i])
        backwards.reverse()
        
        res = []
        for i in range(len(nums)):
            res.append(forward[i] * backwards[i + 1])
        
        return res