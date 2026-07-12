class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}

        for word in strs:
            v = ''.join(sorted(word))
            pairs.setdefault(v,[]).append(word)
        
        return list(pairs.values())
