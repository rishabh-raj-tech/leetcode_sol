class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for x in d:
            if d[x] != d[s[0]]:
                return False
        return True
