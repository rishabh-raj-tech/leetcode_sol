class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_map = {}
        for char in brokenLetters:
            broken_map[char] = True
            
        words = text.split()
        
        valid_word_count = 0
        
        for word in words:
            can_type = True
            
            for char in word:
                if char in broken_map:
                    can_type = False
                    break  
            
            if can_type:
                valid_word_count += 1
                
        return valid_word_count