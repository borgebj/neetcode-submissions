class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        
        for s in strs:

            # create a unique signature based on its 'content'
            # sorted -> make similar words appear the same (eat, tea both becomes 'a' 'e' 't')
            # tuple -> makes it hashable (can use in dict)
            signature = tuple(sorted(s))

            # check if it exists already or add it
            if signature in groups:
                groups[signature].append(s)
            else:
                groups[signature] = [s]

        
        return list(groups.values())