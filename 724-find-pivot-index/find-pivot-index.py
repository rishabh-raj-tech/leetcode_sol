class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        total_sum = prefix[n]
        
        for i in range(n):
            left_sum = prefix[i]
            right_sum = total_sum - prefix[i + 1]
            if left_sum == right_sum:
                return i
                
        return -1