class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        def string_to_map(s: str) -> dict[str, int]:
            result: dict[str, int] = {}
            for ch in s:
                result[ch] = 1 + result.get(ch, 0)
            return result
        
        # Mapear hashmaps de strings con sus indices
        indices: dict[str, list[int]] = {}
        for i, s in enumerate(strs):
            string_map = str(sorted(string_to_map(s).items()))
            indices_list = indices.get(string_map, [])
            indices_list.append(i)
            indices[string_map] = indices_list

        # Recorrer ese hashmap para crear la lista final
        result = []
        for indices_list in indices.values():
            inner_list = []
            for i in indices_list:
                inner_list.append(strs[i])
            result.append(inner_list)
        
        return result





