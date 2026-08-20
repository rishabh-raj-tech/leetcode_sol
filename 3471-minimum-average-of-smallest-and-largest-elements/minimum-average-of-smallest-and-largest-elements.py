class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        li = sorted(nums)
        x = len(li)
        for i in range(x//2):
            averages.append((li[i]+li[x-1-i])/2)

        return min(averages)