class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        score = k
        n = len(nums)
        for i in range(n):
            if score in nums:
                score += k
        return score