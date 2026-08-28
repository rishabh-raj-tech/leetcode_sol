class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l,r = 0,1
        li = []
        while l<len(nums)-1:
            while r<len(nums):
                if nums[l] == -nums[r]:
                    li.append(abs(nums[l]))
                r += 1
            l += 1
            r = l+1
        if len(li)>0:
            return max(li)
        return -1