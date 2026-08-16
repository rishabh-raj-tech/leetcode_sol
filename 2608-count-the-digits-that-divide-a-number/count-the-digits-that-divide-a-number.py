class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            x = n % 10
            if num % x == 0:
                count += 1
            n //= 10
        return count
