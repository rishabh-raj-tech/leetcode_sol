class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        ans = 0
        if s/k >= threshold:
            ans += 1
        for i in range(k,len(arr)):
            s += arr[i] 
            s -= arr[i-k]
            if s/k >= threshold:
                ans += 1
            
        return ans