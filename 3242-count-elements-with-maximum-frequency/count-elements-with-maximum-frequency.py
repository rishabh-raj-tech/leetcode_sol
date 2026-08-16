class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        count = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
        x = max(d.values())

        for j in d:
            if d[j] == x:
                count += 1

        return x * count
