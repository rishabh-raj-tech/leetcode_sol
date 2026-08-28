class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        count = 0
        l,r = 0,len(nums)-1
        while l<r:
            count += int(str(nums[l])+str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            count += nums[l]
        return count
