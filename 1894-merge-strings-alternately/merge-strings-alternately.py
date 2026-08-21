class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        result = ""
        
        while i < len1 or j < len2:
            if i < len1:
                result += word1[i]
                i += 1
            if j < len2:
                result += word2[j]
                j += 1
                
        return result