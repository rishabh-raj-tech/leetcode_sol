class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(ones) < k:
            return ""
        
        ans = ""
        min_len = float('inf')
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            sub_len = len(sub)
            if sub_len < min_len:
                min_len = sub_len
                ans = sub
            elif sub_len == min_len:
                ans = min(ans, sub)
                
        return ans