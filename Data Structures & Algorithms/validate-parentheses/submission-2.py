class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        
        stack = []

        # go through letters
        for c in s:
            
            # -- opening types --
            #   add its closing to stack
            #   '(' ? --> stack = ')'
            if c in pairs:
                stack.append(pairs[c])

            # -- else it is a closing  --

            # if top of stack also has closing, its wrong
            elif len(stack) == 0 or stack[-1] != c:
                return False

            else:
                stack.pop()

        return len(stack) == 0