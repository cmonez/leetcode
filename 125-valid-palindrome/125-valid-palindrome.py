class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        removeAlpha = ''.join(ch for ch in lower if ch.isalnum())
        return removeAlpha[::-1] == removeAlpha
        