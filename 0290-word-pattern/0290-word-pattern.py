class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        char_to_word = {}
        word_to_char ={}

        for c , w in zip(pattern, word):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w
            
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
            
        return True
                    
