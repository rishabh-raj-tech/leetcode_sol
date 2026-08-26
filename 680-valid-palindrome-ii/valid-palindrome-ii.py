class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        b = True
        while i < j:
            if s[i] != s[j]:
                b = False
                break
            i += 1
            j -= 1
        if b == True:
            return True
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        return check(i + 1, j) or check(i, j - 1)
        