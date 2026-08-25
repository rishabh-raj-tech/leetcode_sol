class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans,s = -100000,0
        for i in range(n):
            s += nums[i]
            ans = max(ans, s)
            if s<0:
                s = 0
        return ans