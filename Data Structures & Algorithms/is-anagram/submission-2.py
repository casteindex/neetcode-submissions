class Solution:
    def charCount(self, s: str) -> dict[str, int]:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.charCount(s) == self.charCount(t)