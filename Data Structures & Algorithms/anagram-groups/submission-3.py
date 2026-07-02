class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        def letter_count(string: str) -> tuple(int):
            count = [0,] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            return tuple(count)
        
        # Mapear hashmaps de strings con sus indices
        indices: dict[str, list[int]] = {}
        for i, string in enumerate(strs):
            key = letter_count(string)
            index_list = indices.get(key, [])
            index_list.append(i)
            indices[key] = index_list

        # Recorrer ese hashmap para crear la lista final
        result = []
        for indices_list in indices.values():
            inner_list = []
            for i in indices_list:
                inner_list.append(strs[i])
            result.append(inner_list)
        
        return result





