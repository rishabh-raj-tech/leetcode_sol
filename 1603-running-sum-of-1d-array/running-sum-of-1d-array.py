class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p = [nums[0]]
        for i in range(1, len(nums)):
            p.append(p[i-1] + nums[i])
        return p