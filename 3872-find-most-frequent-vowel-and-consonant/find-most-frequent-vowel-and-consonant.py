class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        max_vowel_freq = 0
        max_consonant_freq = 0
        
        for char, freq in counts.items():
            if char in vowels:
                if freq > max_vowel_freq:
                    max_vowel_freq = freq
            else:
                if freq > max_consonant_freq:
                    max_consonant_freq = freq
        
        return max_vowel_freq + max_consonant_freq