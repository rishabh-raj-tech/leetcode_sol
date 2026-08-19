class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        arr.sort()
        ans = []
        for i in range(len(nums)):
            ans.append(arr.index(nums[i]))
        return ans