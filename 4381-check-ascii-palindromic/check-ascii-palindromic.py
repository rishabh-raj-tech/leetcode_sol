class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_str = ""
        for char in s:
            ascii_val = ord(char)
            binary_val = f"{ascii_val:08b}"
            binary_str += binary_val

        return binary_str == binary_str[::-1]