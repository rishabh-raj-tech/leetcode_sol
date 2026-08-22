class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        add = 0
        pro = 1
        while x > 0:
            add += x % 10
            pro *= x % 10
            x //= 10
        return n % (add + pro) == 0