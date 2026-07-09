class Solution:
    DELIMITER = chr(31) # ASCII unit separator

    def encode(self, strs: List[str]) -> str:
        parts: list[str] = []
        for s in strs:
            parts.append(s)
            parts.append(self.DELIMITER)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = s.split(self.DELIMITER)
        res.pop()
        return res
