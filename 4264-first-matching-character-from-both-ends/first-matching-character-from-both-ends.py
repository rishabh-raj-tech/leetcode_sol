class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i,j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                return i
            else:
                i+= 1
                j-= 1
        return -1