class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, j = 1, n
        ans = 1
        while i <= j:
            mid = (i + j) // 2
            req = (mid * (mid + 1)) // 2
            if req > n:
                j = mid - 1
            else:
                ans = mid
                i = mid + 1
        return ans