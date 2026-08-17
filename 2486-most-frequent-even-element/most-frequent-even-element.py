class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num % 2 == 0:
                counts[num] = counts.get(num, 0) + 1
        
        if not counts:
            return -1
        
        ans = -1
        max_freq = 0
        
        for num, freq in counts.items():
            if freq > max_freq or (freq == max_freq and num < ans):
                ans = num
                max_freq = freq
                
        return ans