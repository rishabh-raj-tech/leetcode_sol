class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        score = k
        while score in s:
            score += k
        return score