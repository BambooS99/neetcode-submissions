import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-z0-9]', '', s.lower())
        reversed = cleaned_s[::-1]
    
        return cleaned_s == reversed