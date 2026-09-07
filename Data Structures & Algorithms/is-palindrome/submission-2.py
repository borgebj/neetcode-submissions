class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean + rebuild string
        s = ''.join(c.lower() for c in s if c.isalnum())

        # compare with its reverse
        return s == s[::-1]