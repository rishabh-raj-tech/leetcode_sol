class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        li = []
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for x in d:
            if d[x] == 1:
                li.append(x)

        return sum(li)