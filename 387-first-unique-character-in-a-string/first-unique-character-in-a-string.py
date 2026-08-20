class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for x in d:
            if d[x] == 1:
                return s.index(x)

        return -1