class Solution:
    
    # encoding/decoding is swapping start and ends
    def swappy(self, a):
        n = len(a)
        a = list(a)
        for i in range(n-1, int(n/2), -1):
            a[n-i], a[i] = a[i], a[n-i]

        return "".join(a)

    def encode(self, strs: List[str]) -> str:
        a = [self.swappy(s) for s in strs]
        return "".join(str(len(s)) + "#" + s for s in a)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        # go through s, find start and ends of words
        while i < len(s):
            length_end = s.index("#", i) 
            length = int(s[i:length_end])

            start = length_end +1 
            end = start + length

            word = self.swappy(s[start:end])
            result.append(word)
            i = end

        return result