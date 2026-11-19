class Solution:
    def isPalindrome(self, s: str) -> bool:

        for letter in s:
            if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                s = s.replace(letter, "")

        s = s.lower()


        return s == s[::-1]
        