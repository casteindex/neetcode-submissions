class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = {chr(_) for _ in range(ord('a'), ord('z') + 1)}
        nums = {chr(_) for _ in range(ord('0'), ord('9') + 1)}
        validChars = letters | nums

        s_lower = s.lower()

        l, r = 0, len(s) - 1
        while l <= r:
            if s_lower[l] not in validChars:
                l += 1
                continue
            if s_lower[r] not in validChars:
                r -= 1
                continue
            if s_lower[l] != s_lower[r]:
                return False
            l += 1
            r -= 1
        return True