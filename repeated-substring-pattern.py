class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        twice_s = s+s
        modified_s = twice_s[1:-1]
        return s in modified_s
