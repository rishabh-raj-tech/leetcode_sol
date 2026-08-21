class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = 51
        nums.sort()
        i,j = 0, len(nums) - 1
        while i<j:
            avg = min(avg, ((nums[i] + nums[j])/2))
            i += 1
            j-= 1

        return avg
