from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter()
        n = len(nums)
        
        for i in range(n - k + 1):
            subarray_unique_elements = set(nums[i : i + k])
            for num in subarray_unique_elements:
                freq[num] += 1
        
        valid_candidates = [num for num, count in freq.items() if count == 1]
        
        return max(valid_candidates) if valid_candidates else -1