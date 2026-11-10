class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters_s = {}

        letters_t = {}

        for letter in s: 
            if letter in letters_s: 
                letters_s[letter] += 1
            else: 
                letters_s[letter] = 0

        for letter in t: 
            if letter in letters_t: 
                letters_t[letter] += 1
            else: 
                letters_t[letter] = 0
                
        return letters_s == letters_t