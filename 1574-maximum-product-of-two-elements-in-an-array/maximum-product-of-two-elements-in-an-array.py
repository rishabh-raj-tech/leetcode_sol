class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = sorted(nums)
        y = len(x)
        p = 1
        for i in range(y - 1, y - 3, -1):
            p *= (x[i] - 1)

        return p
