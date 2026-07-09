class Solution:
    DELIMITER = chr(31) # ASCII unit separator

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append(self.DELIMITER)
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != self.DELIMITER:
                j += 1
            size = int(s[i:j])
            res.append(s[j + 1 : j + 1 + size])
            i = j + 1 + size
        return res
