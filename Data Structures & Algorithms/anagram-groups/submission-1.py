class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        
        for s in strs:

            # create a unique signature based on its 'content'
            # sorted -> make similar words appear the same (eat, tea both becomes 'a' 'e' 't')
            # tuple -> makes it hashable (can use in dict)
            signature = tuple(sorted(s))

            # add string to group using signature
            groups[signature].append(s)

        
        return list(groups.values())

# visualisation
#
# input = ["abc", "bcd", "cab", "dcc"]
#
# "abc" -> ('a', 'b', 'c')  #1
# "bcd" -> ('b', 'c', 'd')  #2
# "cab" -> ('a', 'b', 'c')  #1
# "dcc" -> ('c', 'c', 'd')  #3
#
# groups = [('a','b','c'): ["abc", "cab"], ('b','c','d'): ["bcd"], ('c','c','d'): ["bcd"]]
#
# simplified, 3 unique signatures:
#
# groups = [#1: ["abc", "cab"], #2: ["bcd"], #3: ["bcd"]]