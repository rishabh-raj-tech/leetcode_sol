class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        li = sorted(prices)
        s = 0
        for i in range(0,2):
            s += li[i]
        if s <= money:
            return money - s
        else:
            return money

