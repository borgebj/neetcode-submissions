class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = {}

        # scan S
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

        # scan T
        for char in t:
            if char in seen:
                seen[char] -= 1
            else:
                return False

        return not any(seen.values())
