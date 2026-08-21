class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        nums.sort()
        i,j = 0, len(nums) - 1
        while i<j:
            avg.append(((nums[i] + nums[j])/2))
            i += 1
            j-= 1

        return min(avg)
