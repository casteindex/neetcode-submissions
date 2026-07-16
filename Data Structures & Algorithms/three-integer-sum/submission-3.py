class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        i = 0
        while i <= len(nums) - 3:
            startNum = nums[i]
            diff = 0 - startNum

            # Encontrar dos números que sumen diff 
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum < diff:
                    l += 1
                elif currSum > diff:
                    r -= 1
                else: # Dos números encontrados
                    res.append([nums[i], nums[l], nums[r]])
                    # Ver si hay otros para el mismo inicio
                    currL, currR = nums[l], nums[r]
                    while l < r and nums[l] == currL:
                        l += 1
                    while r > l and nums[r] == currR:
                        r -= 1
            
            # Encontrar nuevo número inicial
            while i < len(nums) and nums[i] == startNum:
                i += 1

        return res