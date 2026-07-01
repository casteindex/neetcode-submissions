class Solution:
    def charCount(self, s: str) -> dict[str, int]:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.charCount(s) == self.charCount(t)