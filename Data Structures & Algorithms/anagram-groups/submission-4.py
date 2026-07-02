class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Contar cantidad de cada letra
        def countLetters(string: str) -> tuple[int]:
            count = [0,] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            return tuple(count)
        
        # Mapear palabras para cada set de cant letras
        group: [tuple[int], list[str]] = {}
        for i, string in enumerate(strs):
            key: tuple[int] = countLetters(string)
            word_list: list[str] = group.get(key, [])
            word_list.append(strs[i])
            group[key] = word_list
        
        return list(group.values())

