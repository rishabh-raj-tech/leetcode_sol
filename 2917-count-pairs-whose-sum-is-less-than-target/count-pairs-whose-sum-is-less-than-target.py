class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r = 0,len(nums)- 1
        x = r
        c = 0
        while l <= r:
            if nums[l] + nums[r] >= target:
                r -= 1
            elif nums[l] + nums[r] < target:
                while l < r:
                    r -= 1
                    c += 1
                r = x
                l += 1
        return c
                
