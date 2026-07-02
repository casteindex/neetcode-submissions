class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Contar cantidad de cada letra
        def countLetters(string: str) -> tuple[int]:
            count = [0,] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            return tuple(count)
        
        # Mapear palabras para cada set de cant letras
        group: dict[tuple[int], list[str]] = {}
        for s in strs:
            key: tuple[int] = countLetters(s)
            group.setdefault(key, []).append(s)
        
        return list(group.values())

